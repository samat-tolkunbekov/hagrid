class HelloWorld:
    def say_hello(self) -> str:
        return 'Hello world!'
    
    def say_multiple_hellos(self) -> list:
        return [
            'Hello word!',
            'Hello milky way!',
            'Hello sun!',
            'Hello earth!',
        ]
    
    def say_hello_as_json(self) -> dict:
        return {
            'message': 'Hello world!',
            'sender': 'me',
            'receiver': 'you',
        }
    
hello_world = HelloWorld()
print(hello_world.say_hello())