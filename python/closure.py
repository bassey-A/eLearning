import datetime


def make_logger(prefix: str, log_level: str = "INFO"):
    """
    Function factory that creates and returns a customized logger function.
    The returned logger will have a specific prefix and log level.
    """
    # These variables (prefix, log_level) will be "closed over" by the inner function.
    print(
        f"--- Logger factory: Creating logger with prefix='{prefix}', level='{log_level}' ---"
    )

    def logger_function(message: str, *args, **kwargs):
        """
        This is the actual logger function (a closure).
        It logs the given message along with any additional *args or **kwargs.
        It uses the 'prefix' and 'log_level' captured from its enclosing scope.
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_entry_parts = [
            f"[{timestamp}]",
            f"[{log_level.upper()}]",
            f"[{prefix}]",
            message,
        ]

        # Add any extra positional arguments
        if args:
            positional_details = ", ".join(map(str, args))
            log_entry_parts.append(f"| Positional Data: {positional_details}")

        # Add any extra keyword arguments
        if kwargs:
            keyword_details = ", ".join(
                f"{key}={value}" for key, value in kwargs.items()
            )
            log_entry_parts.append(f"| Keyword Data: {keyword_details}")

        final_log_entry = " ".join(log_entry_parts)
        print(final_log_entry)
        # In a real application, you might write this to a file, send to a logging service, etc.

    return logger_function  # Return the inner function


# --- Using the function factory ---

# Create different logger instances
user_service_logger = make_logger("UserService", log_level="DEBUG")
payment_logger = make_logger("PaymentService")  # Uses default log_level "INFO"
critical_system_logger = make_logger("SystemCore", log_level="CRITICAL")

print("\n--- Using the created logger functions ---")

# Now, call the returned logger functions (closures)
# Notice how they can accept different sets of *args and **kwargs
user_service_logger(
    "User login attempt", "user_id=123", "ip=192.168.1.100", source_module="auth.py"
)
# "user_id=123" and "ip=..." become part of *args (as they are positional here to logger_function after 'message')
# 'source_module' becomes a kwarg

user_service_logger("User profile update", user_id=456, field_updated="email_address")
# Here, user_id and field_updated are keyword arguments passed via **kwargs

payment_logger(
    "Payment received", transaction_id="txn_abc123", amount=50.75, currency="NGN"
)

payment_logger(
    "Payment refund processed",
    "original_txn_id=txn_def456",
    amount=20.00,
    currency="NGN",
    reason="item_returned",
)

critical_system_logger(
    "Critical error detected!",
    "Error Code: 5003",
    component="DatabaseConnector",
    details={"message": "Connection timeout", "retry_attempts": 3},
)
