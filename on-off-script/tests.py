#!/usr/bin/env python
# helloworld.py

from unittest import TestCase
from unittest.mock import patch

from helloworld import do_hello, URL

class FakeResult:
    text = '<title>"Hello, World! program - wikipedia"</title>'

class TextHelloWorld(TestCase):
  
    @patch('request.get')
    def test_helloworld():
        """test hello-world function"""
        mock_get.return_value = FakeResult()
        do_hello()
        mock_get.assert_called_with(URL)

if __name__ == "__main__":
    from unittest import main
    main()