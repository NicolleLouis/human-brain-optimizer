class LogRequest:
    def __init__(self, logger_name, log_type, log_value):
        self.logger_name = logger_name
        self.log_type = log_type
        self.log_value = log_value

    def __str__(self):
        return f"{self.logger_name}: {self.log_type} -> {self.log_value}"
