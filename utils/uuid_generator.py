import uuid

def generate_uuid()->str:
    try:
        return uuid.uuid5(uuid.uuid4(),uuid.uuid4().__str__()).__str__()
    except Exception:
        raise

if __name__=="__main__":
    print(generate_uuid())