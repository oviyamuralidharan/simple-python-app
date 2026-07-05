from app import greet

def test_greet():
    assert greet() == "Hello from Jenkins CI/CD Pipeline!"

print("✅ Test Passed")
