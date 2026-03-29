from datastore import store_value, get_value, delete_value as datastore_delete_value, list_keys

def process_and_store(key, raw_value):
    processed_value = raw_value.strip().upper()
    store_value(key, processed_value)
    return processed_value


def retrieve_processed(key):
    value = get_value(key)
    if value is None:
        return None
    return value.lower()


def update_value(key, raw_value):
    store_value(key, raw_value)
    

def delete_value(key):
    if datastore_delete_value(key):
        return True
    return False


def list_all_keys():
    return list_keys()
