try:
    result = int("abc")
except ValueError:
    print("ValueError: Cannot convert 'abc' to an integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
