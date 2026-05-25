import pytest

def test_score_increments(snowman_page, db):
    previous_score = snowman_page.get_current_score()
    word = snowman_page.get_word()
    db.execute("SELECT spanish FROM word_pairs WHERE english = %s", (word,))
    translated_word = db.fetchone()[0]
    snowman_page.input_word(translated_word)
    snowman_page.click_continue()
    snowman_page.wait_for_score_update(previous_score)
    new_score = snowman_page.get_current_score()
    assert new_score == previous_score + 1

def test_score_reset_on_wrong_answer(snowman_page, db):
    alpha = set("abcdefghijklmnopqrstuvwxyz")
    previous_score = snowman_page.get_current_score()
    word = snowman_page.get_word()
    db.execute("SELECT spanish FROM word_pairs WHERE english = %s", (word,))
    translated_word = db.fetchone()[0]
    snowman_page.input_word(translated_word)
    snowman_page.click_continue()
    snowman_page.wait_for_score_update(previous_score)
    new_score = snowman_page.get_current_score()
    previous_score = new_score
    word = snowman_page.get_word()
    db.execute("SELECT spanish FROM word_pairs WHERE english = %s", (word,))
    translated_word = db.fetchone()[0]
    alpha = alpha.difference(set(translated_word))
    wrong_word = list(alpha)[:4]
    print(translated_word)
    print(wrong_word)
    snowman_page.input_word(wrong_word)
    snowman_page.click_continue()
    snowman_page.wait_for_score_update(previous_score)
    new_score = snowman_page.get_current_score()
    assert new_score == 0