import spacy
from spacy.language import Language
import re

@Language.component("specificMoves")
def specificMoves(doc):
    new_ents = []
    expression = "(?:(?:[udbnf]{0,10}|([udbnf]+[\s,.+]*){0,10}|(sway)?|(dpd)?|(ss)?)?[\s,]*[1-4](?:\s*[,+-]\s*[1-4])*)+|((?:[1-4](?:\s*[,+-]\s*[1-4])*)+)"
    for match in re.finditer(expression, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end, label = "SPECIFIC_MOVE")
        if span is not None:
            new_ents.append(span)
    doc.ents = list(doc.ents) + new_ents
    return doc