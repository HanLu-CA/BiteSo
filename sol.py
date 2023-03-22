import solara


@solara.component
def Page():
    sentence, set_sentence = solara.use_state("Solara makes our team more productive.")
    word_limit, set_word_limit = solara.use_state(10)
    word_count = len(sentence.split())

    solara.SliderInt("Word limit", value=word_limit, on_value=set_word_limit, min=2, max=20)
    solara.InputText(label="Your sentence", value=sentence, on_value=set_sentence,
                        continuous_update=True)

    if word_count >= int(word_limit):
        solara.Error(f"With {word_count} words, you passed the word limit of {word_limit}.")
    elif word_count >= int(0.8 * word_limit):
        solara.Warning(f"With {word_count} words, you are close to the word limit of {word_limit}.")
    else:
        solara.Success("Great short writing!")

# In a Jupyter notebook, put this at the end of your cell:
# Page()