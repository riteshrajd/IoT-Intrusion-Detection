import torch
import torch.nn as nn

class IntrusionDetectionLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes, num_layers=1, dropout=0.2):
        """
        LSTM for Time Series Intrusion Detection.
        
        Args:
            input_size (int): Number of features in each packet (e.g., 46)
            hidden_size (int): Number of hidden units in LSTM layer
            num_classes (int): Number of output classes (e.g., 8 main labels or 34 sub-labels)
            num_layers (int): Number of stacked LSTM layers
            dropout (float): Dropout probability
        """
        super(IntrusionDetectionLSTM, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        # Batch_first=True expects input of shape (batch_size, seq_length, input_size)
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, 
                            batch_first=True, dropout=dropout if num_layers > 1 else 0)
                            
        self.fc = nn.Linear(hidden_size, num_classes)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x):
        # x shape: (batch_size, seq_length, input_size)
        
        # Initialize hidden state and cell state
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        
        # Forward propagate LSTM
        out, _ = self.lstm(x, (h0, c0))
        
        # Extract the output of the last time step
        # out shape: (batch_size, seq_length, hidden_size)
        # We want the last sequence step
        out = out[:, -1, :]
        
        out = self.dropout(out)
        out = self.fc(out)
        return out


class IntrusionDetectionGRU(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes, num_layers=1, dropout=0.2):
        """
        GRU for Time Series Intrusion Detection.
        Slightly faster than LSTM, often similar performance for network data.
        """
        super(IntrusionDetectionGRU, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        self.gru = nn.GRU(input_size, hidden_size, num_layers, 
                          batch_first=True, dropout=dropout if num_layers > 1 else 0)
                          
        self.fc = nn.Linear(hidden_size, num_classes)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x):
        # x shape: (batch_size, seq_length, input_size)
        
        # Initialize hidden state
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        
        # Forward propagate GRU
        out, _ = self.gru(x, h0)
        
        # Extract the output of the last time step
        out = out[:, -1, :]
        
        out = self.dropout(out)
        out = self.fc(out)
        return out


# Utility to get the model
def get_model(model_type="lstm", input_size=46, hidden_size=64, num_classes=8, num_layers=1):
    if model_type.lower() == "lstm":
        return IntrusionDetectionLSTM(input_size, hidden_size, num_classes, num_layers)
    elif model_type.lower() == "gru":
        return IntrusionDetectionGRU(input_size, hidden_size, num_classes, num_layers)
    else:
        raise ValueError("model_type must be either 'lstm' or 'gru'")
