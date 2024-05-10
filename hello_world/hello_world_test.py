from hello_world import HelloWorld

class TestHelloWorld:
    def test_say_hello(self):
        assert 'Hello world!' == HelloWorld().say_hello()

    def test_say_multiple_hellos(self):
        expected = [
            'Hello word!',
            'Hello milky way!',
            'Hello sun!',
            'Hello earth!',
        ]

        assert expected == HelloWorld().say_multiple_hellos()

    def test_say_json_hello(self):
        expected = {
            'message': 'Hello world!',
            'sender': 'me',
            'receiver': 'you',
        }

        assert expected == HelloWorld().say_hello_as_json()