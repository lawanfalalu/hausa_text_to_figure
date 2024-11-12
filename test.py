from HausaNum2WordRepresentation import kalma
def test_to_words():
    converter = kalma()

    # Test integers
    assert converter.fassara(263273) == "dubu ɗari biyu da sittin da uku da ɗari biyu da saba'in da uku", "Test failed for 263273"
    assert converter.fassara(703494) == "dubu ɗari bakwai da uku da ɗari huɗu da casa'in da huɗu", "Test failed for 703494"
    assert converter.fassara(284047) == "dubu ɗari biyu da tamanin da huɗu da arba'in da bakwai", "Test failed for 284047"
    assert converter.fassara(163241) == "dubu ɗari ɗaya da sittin da uku da ɗari biyu da arba'in da ɗaya", "Test failed for 163241"
    assert converter.fassara(292225) == "dubu ɗari biyu da casa'in da biyu da ɗari biyu da ashirin da biyar", "Test failed for 292225"
    assert converter.fassara(435686) == "dubu ɗari huɗu da talatin da biyar da ɗari shida da tamanin da shida", "Test failed for 435686"
    assert converter.fassara(117640) == "dubu ɗari ɗaya da goma sha-bakwai da ɗari shida da arba'in", "Test failed for 117640"
    assert converter.fassara(354443) == "dubu ɗari uku da hamsin da huɗu da ɗari huɗu da arba'in da uku", "Test failed for 354443"
    assert converter.fassara(93191) == "dubu casa'in da uku da ɗari ɗaya da casa'in da ɗaya", "Test failed for 93191"
    assert converter.fassara(614505) == "dubu ɗari shida da goma sha-huɗu da ɗari biyar da biyar", "Test failed for 614505"


    # Test floats
    assert converter.fassara(5961.6465) == "dubu biyar da ɗari tara da sittin da ɗaya da ɗigo shida huɗu shida biyar", "Test failed for 5961.6465"
    assert converter.fassara(3632.901) == "dubu uku da ɗari shida da talatin da biyu da ɗigo tarasifili ɗaya", "Test failed for 3632.901"
    assert converter.fassara(848.2051) == "ɗari takwas da arba'in da takwas da ɗigo biyusifili biyar ɗaya", "Test failed for 848.2051"
    assert converter.fassara(4675.8452) == "dubu huɗu da ɗari shida da saba'in da biyar da ɗigo takwas huɗu biyar biyu", "Test failed for 4675.8452"
    assert converter.fassara(1064.7271) == "dubu ɗaya da sittin da huɗu da ɗigo bakwai biyu bakwai ɗaya", "Test failed for 1064.7271"
    assert converter.fassara(1101.5441) == "dubu ɗaya da ɗari ɗaya da ɗaya da ɗigo biyar huɗu huɗu ɗaya", "Test failed for 1101.5441"
    assert converter.fassara(810.0693) == "ɗari takwas da goma da ɗigo sifili shida tara uku", "Test failed for 810.0693"
    assert converter.fassara(7053.7745) == "dubu bakwai da hamsin da uku da ɗigo bakwai bakwai huɗu biyar", "Test failed for 7053.7745"
    assert converter.fassara(4980.9179) == "dubu huɗu da ɗari tara da tamanin da ɗigo tara ɗaya bakwai tara", "Test failed for 4980.9179"
    assert converter.fassara(9173.8495) == "dubu tara da ɗari ɗaya da saba'in da uku da ɗigo takwas huɗu tara biyar", "Test failed for 9173.8495"

    print("All tests passed.")

if __name__ == "__main__":
    test_to_words()