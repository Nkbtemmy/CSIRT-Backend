

# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()
# from django.core.exceptions import ImproperlyConfigured


# def get_env_variable(env_variable, default=None, required=False):
#     """Helper function to fetch env variables

#     Args:
#         env_variable (str): Env variable to be fetched
#         default (str, optional): Default value of the env variable. Defaults to None.
#         required (bool, optional): Defines whether or not the variable is required. Defaults to False.

#     Raises:
#         ImproperlyConfigured: Exception raised when a variable is required but not set

#     Returns:
#         [type]: Set value of the env variable
#     """
#     value = os.getenv(env_variable, default)
#     if required and not value:
#         error_msg = f"Set the {env_variable} environment variable"
#         raise ImproperlyConfigured(error_msg)
#     return value

import os
from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured

# Load environment variables from .env file
load_dotenv()


def get_env_variable(env_variable, default=None, required=False):
    """Helper function to fetch env variables

    Args:
        env_variable (str): Env variable to be fetched
        default (str, optional): Default value of the env variable. Defaults to None.
        required (bool, optional): Defines whether or not the variable is required. Defaults to False.

    Raises:
        ImproperlyConfigured: Exception raised when a variable is required but not set

    Returns:
        [type]: Set value of the env variable
    """
    # First, try fetching from .env file
    value = os.getenv(env_variable, default)

    # If required and not found in .env file or environment, raise ImproperlyConfigured
    if required and value == default:
        error_msg = f"Set the {env_variable} environment variable"
        raise ImproperlyConfigured(error_msg)

    return value
