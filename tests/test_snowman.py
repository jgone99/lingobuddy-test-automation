import pytest

@pytest.mark.ui
@pytest.mark.game
def test_score_increments(snowman_page, db, reset_snowman_progress):
    previous_score = snowman_page.get_current_score()
    snowman_page.answer_correctly(db)
    snowman_page.wait_for_current_score_update(previous_score)
    new_score = snowman_page.get_current_score()
    assert new_score == previous_score + 1

@pytest.mark.ui
@pytest.mark.game
def test_score_reset_on_wrong_answer(snowman_page, db, reset_snowman_progress):
    # answering correctly first to get a non-zero socre to reset from
    previous_score = snowman_page.get_current_score()
    snowman_page.answer_correctly(db)
    snowman_page.wait_for_current_score_update(previous_score)
    new_score = snowman_page.get_current_score()
    
    previous_score = new_score
    snowman_page.answer_incorrectly(db)
    snowman_page.wait_for_current_score_update(previous_score)
    new_score = snowman_page.get_current_score()
    assert new_score == 0

@pytest.mark.ui
@pytest.mark.game
def test_high_score_persists_on_wrong_answer(snowman_page, db, reset_snowman_progress):
    current_score = snowman_page.get_current_score()
    high_score = snowman_page.get_high_score()
    snowman_page.answer_correctly(db)
    snowman_page.wait_for_current_score_update(current_score)

    current_score = snowman_page.get_current_score()
    snowman_page.answer_incorrectly(db)
    assert snowman_page.get_high_score() == high_score

@pytest.mark.xfail(reason="Bug: high score UI does not update until page refresh. Score is persisted correctly "
"in the database but the displayed value requires a page reload to reflect the updated high score.")
@pytest.mark.ui
@pytest.mark.game
def test_high_score_increments(snowman_page, db, reset_snowman_progress):
    high_score = snowman_page.get_high_score()
    for i in range(high_score + 1):
        current_score = snowman_page.get_current_score()
        snowman_page.answer_correctly(db)
        snowman_page.wait_for_current_score_update(current_score)
    assert snowman_page.get_high_score() == high_score + 1