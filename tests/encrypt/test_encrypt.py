import pytest

from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(31, 4)
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", "not_a_key")
    assert encrypt_message("teste", 4) == "e_tset"
    assert encrypt_message("teste", 1) == "t_etse"
    assert encrypt_message("teste", 9) == "etset"
