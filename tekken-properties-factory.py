import spacy
from spacy.language import Language
from spacy.tokens import Doc
from spacy.matcher import PhraseMatcher

@Language.component("tekkenSpecific")
def tekkenSpecific(doc):
    nlp = spacy.load("en_core_web_sm")
    matcher_attr = "TEXT" 
    new_ents = []
    matcher = PhraseMatcher(nlp.vocab, attr = matcher_attr)
    props = ['high crushes', 'high crushing', 'high crush','low crush', 'low crushing', 'low crushes', 'guard break', 'grounded', 'guard crush', 'guard crushes', 'guard crushing','flip over', 'in crouch',  'chargable', 'holdable', 'blue spark', 'blue sparks', 'knocks down']
    moves = ['heat burst', 'heat smash', 'chain throw', 'chain grab', 'power crush','homing', 'armor', 'armored', 'parry', 'sabaki', 'instant screw', 'instant tornado', 'rage art']
    patterns = [nlp.make_doc(text) for text in props]
    movePatterns = [nlp.make_doc(text) for text in moves]
    matcher.add("PROPERTIES", patterns)
    matcher.add("MOVE_TYPES", movePatterns)
    matches = matcher(doc)
    for match_id, start, end in matches:
        span = doc[start:end]
        # property
        if match_id == 17494066980514271985:
            span = doc.char_span(span.start_char, span.end_char, label = "MOVE_PROPERTY")
        # move type
        elif match_id == 9842506821441691883:
            span = doc.char_span(span.start_char, span.end_char, label = "MOVE_TYPE")
        if span is not None:
            new_ents.append(span)

    doc.ents = list(doc.ents) + new_ents