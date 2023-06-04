from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # testando os tipos incorretos para key e message
    with pytest.raises(TypeError):
        encrypt_message("edvaldo", "edvaldo") == "tipo inválido para key"
        encrypt_message(1223, "img") == "tipo inválido para message"

    # testando com key ímpar
    assert encrypt_message("edvaldo", 3) == "vde_odla"

    # testando com key par
    assert encrypt_message("abcdefghi", 4) == "ihgfe_dcba"

    # testando com Key maior que a mensagem
    assert encrypt_message("abcdefghi", 90) == "ihgfedcba"
