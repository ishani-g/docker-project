import logging
import platform
import os
import time
import psutil  # Import psutil library for system monitoring
from datetime import datetime

def get_os_info():
    """Fetch information about the operating system."""
    os_info = {
        "processor": platform.processor(),
    }
    return os_info

def setup_logging():
    """Set up logging configuration."""
    log_file = "/logs/os_info.txt"
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def log_os_info():
    """Log operating system information."""
    os_info = get_os_info()
    logging.info("Operating System Information:")
    for key, value in os_info.items():
        logging.info(f"{key}: {value}")

    # Log running processes
    logging.info("Running Processes:")
    for proc in psutil.process_iter():
        logging.info(f"PID: {proc.pid}, Name: {proc.name()}, CPU Usage: {proc.cpu_percent()}%, Memory Usage: {proc.memory_percent()}%")

    # Log CPU usage
    cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
    logging.info(f"CPU Usage: {cpu_usage}%")

    # Log memory usage
    memory_usage = psutil.virtual_memory()
    logging.info(f"Memory Usage: Total: {memory_usage.total} bytes, Available: {memory_usage.available} bytes")

if __name__ == "__main__":
    setup_logging()  # Initialize logging immediately upon execution
    log_os_info()   # Log OS information
    # Log every 3 minutes
    while True:
        time.sleep(180)  # Sleep for 3 minutes (180 seconds)
        log_os_info()     # Log OS information every 3 minutes
