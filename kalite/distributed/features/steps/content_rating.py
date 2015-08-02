from behave import *
from kalite.testing.behave_helpers import *

RATING_CONTAINER_ID = "rating-container"
TEXT_CONTAINER_ID = "text-container"
STAR_CONTAINER_IDS = (
    "star-container-1",
    "star-container-2",
    "star-container-3",
)
SUBMIT_ID = "rating-submit"

@then(u'my feedback is displayed')
def impl(context):
    for star_id in STAR_CONTAINER_IDS:
        star_el = find_id_with_wait(context, star_id)
        assert elem_is_visible_with_wait(context, star_el), "Star rating form with id '{0}' not visible".format(star_id)
    actual = get_text_feedback(context)
    expected = context.text_feedback
    assert actual == expected, "Expected:\n\t '{expected}'\n but saw\n\t '{actual}'\n in feedback form".format(
        expected=expected, actual=actual)

@then(u'I see a feedback form')
def impl(context):
    feedback_form_container = find_id_with_wait(context, RATING_CONTAINER_ID)
    assert elem_is_visible_with_wait(context, feedback_form_container), "Rating form is not visible."

@given(u'some user feedback exists')
def impl(context):
    assert False

@then(u'the user feedback is present')
def impl(context):
    assert False

@then(u'I see a blank form')
def impl(context):
    assert False

@when(u'I edit my feedback')
def impl(context):
    assert False

@when(u'I fill out the form')
def impl(context):
    enter_star_ratings(context)
    text_feedback = context.text_feedback = "This stuff is great, A+++"
    enter_text_feedback(context, text_feedback)
    submit_feedback(context)

@given(u'I am on a content page')
def impl(context):
    go_to_content_item(context)

@given(u'I have filled out a feedback form')
def impl(context):
    assert False

@then(u'I see an edit button')
def impl(context):
    assert False

@then(u'I see a delete button')
def impl(context):
    assert False

@when(u'I delete my feedback')
def impl(context):
    assert False

@when(u'I export csv data')
def impl(context):
    assert False

@then(u'my edited feedback is displayed')
def impl(context):
    assert False


def enter_star_ratings(context):
    """
    Enters a value for all three star rating forms, on a new form
    :param context: behave context
    :return: nothing
    """
    for id_ in STAR_CONTAINER_IDS:
        rate_id(context, id_)


def rate_id(context, id, val=3):
    """
    Enter a star rating given the id of the container
    :param context: behave context
    :param id: id of the container element
    :return: nothing
    """
    container = find_id_with_wait(context, id)
    rating_val_class = "rating-val-{0}".format(val)

    def get_rating_el(driver):
        try:
            return container.find_element_by_class_name(rating_val_class)
        except NoSuchElementException:
            return False

    rating_el = WebDriverWait(context.browser, 10).until(get_rating_el)
    rating_el.click()


def enter_text_feedback(context, text_feedback):
    """
    Enter text feedback into feedback form
    :param context: behave context
    :param text_feedback: str, the feedback to be entered
    :return: nothing
    """
    text_container = find_id_with_wait(context, TEXT_CONTAINER_ID)
    input_field = text_container.find_element_by_class_name("rating-text-feedback")
    input_field.send_keys(text_feedback)


def submit_feedback(context):
    """
    Submit feedback form
    :param context: behave context
    :return: nothing
    """
    submit_btn = find_id_with_wait(context, SUBMIT_ID)
    submit_btn.click()


def get_text_feedback(context):
    """
    Get the text feedback displayed after the feedback form is filled out
    :param context: behave context
    :return: a str with the text feedback displayed.
    """
    text_el = find_id_with_wait(context, TEXT_CONTAINER_ID)
    return text_el.text