import capitals as caps


def test_get_fuzzy_string_match():
    expected = "Alabama"
    actual = caps.get_fuzzy_match("alama", ["AL", "Califonria", "Alaska", "Arkansas", "Alabama"], 3)
    assert expected == actual

def test_match_search():
    expected = "California"
    actual = caps.match_search_string("califor")
    assert expected == actual


def test_match_search_abbrev():
    expected = "New Mexico"
    actual = caps.match_search_string("new m")
    assert expected == actual

