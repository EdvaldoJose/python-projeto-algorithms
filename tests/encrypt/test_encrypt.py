from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message('edvaldo', 'edvaldo') == 'tipo invalido para key'
        encrypt_message(1223, 'img') == 'tipo invalido para message'


assert encrypt_message('edvaldo', 3) == 'vde_aldo'
#  testando com a key impar

assert encrypt_message('abcdefghi', 4) == 'ihgfe_dcba'
# testando com a key par

assert encrypt_message('abcdefghi', 100) == 'ihgfedcba'
