def class_to_json(obj):
    """
    Returns a dictionary description with a simple data structure for JSON serialization of an object
    """
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    elif isinstance(obj, (list, tuple)):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, (str, int, bool, type(None))):
        return obj
    else:
        raise TypeError("Object of type '{}' is not JSON serializable".format(type(obj).__name__))
