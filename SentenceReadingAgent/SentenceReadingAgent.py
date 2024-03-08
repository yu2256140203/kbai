import re
import string

DEBUG = 1
LEMMA_DICT = \
{'Serena': ('Serena', 'PROPN'), '\n': ('\n', 'SPACE'), 'Andrew': ('Andrew', 'PROPN'), 'Bobbie': ('Bobbie', 'PROPN'), 'Cason': ('Cason', 'PROPN'), 'David': ('David', 'PROPN'), 'Farzana': ('Farzana', 'PROPN'), 'Frank': ('Frank', 'PROPN'), 'Hannah': ('Hannah', 'PROPN'), 'Ida': ('Ida', 'PROPN'), 'Irene': ('Irene', 'PROPN'), 'Jim': ('Jim', 'PROPN'), 'Jose': ('Jose', 'PROPN'), 'Keith': ('Keith', 'PROPN'), 'Laura': ('Laura', 'PROPN'), 'Lucy': ('Lucy', 'PROPN'), 'Meredith': ('Meredith', 'PROPN'), 'Nick': ('Nick', 'PROPN'), 'Ada': ('Ada', 'PROPN'), 'Yeeling': ('Yeeling', 'PROPN'), 'Yan': ('Yan', 'PROPN'), 'the': ('the', 'PRON'), 'of': ('of', 'ADP'), 'to': ('to', 'ADP'), 'and': ('and', 'CCONJ'), 'a': ('a', 'PRON'), 'in': ('in', 'ADP'), 'is': ('be', 'AUX'), 'it': ('it', 'PRON'), 'It': ('It', 'PRON'), 'you': ('you', 'PRON'), 'that': ('that', 'SCONJ'), 'he': ('he', 'PRON'), 'was': ('be', 'AUX'), 'for': ('for', 'ADP'), 'on': ('on', 'ADP'), 'are': ('be', 'AUX'), 'with': ('with', 'ADP'), 'as': ('as', 'ADP'), 'I': ('I', 'PRON'), 'his': ('his', 'PRON'), 'they': ('they', 'PRON'), 'be': ('be', 'VERB'), 'at': ('at', 'ADP'), 'one': ('one', 'NUM'), 'have': ('have', 'VERB'), 'this': ('this', 'PRON'), 'This': ('This', 'PRON'),'from': ('from', 'ADP'), 'or': ('or', 'CCONJ'), 'had': ('have', 'VERB'), 'by': ('by', 'ADP'), 'hot': ('hot', 'ADJ'), 'but': ('but', 'CCONJ'), 'some': ('some', 'DET'), 'what': ('what', 'SCONJ'), 'What': ('what', 'SCONJ'),'there': ('there', 'PRON'), 'There': ('There', 'PRON'), 'we': ('we', 'PRON'), 'can': ('can', 'AUX'), 'out': ('out', 'ADP'), 'other': ('other', 'ADJ'), 'were': ('be', 'AUX'), 'all': ('all', 'ADV'), 'your': ('your', 'PRON'), 'when': ('when', 'SCONJ'), 'When': ('when', 'SCONJ'), 'up': ('up', 'NOUN'), 'use': ('use', 'VERB'), 'word': ('word', 'NOUN'), 'how': ('how', 'SCONJ'), 'How': ('how', 'SCONJ'), 'said': ('say', 'VERB'), 'an': ('an', 'DET'), 'each': ('each', 'DET'), 'she': ('she', 'PRON'), 'She': ('She', 'PROPN'), 'which': ('which', 'PRON'), 'do': ('do', 'AUX'), 'their': ('their', 'PRON'), 'Their': ('Their', 'PRON'),'time': ('time', 'NOUN'), 'if': ('if', 'SCONJ'), 'will': ('will', 'AUX'), 'way': ('way', 'NOUN'), 'about': ('about', 'ADV'), 'many': ('many', 'ADJ'), 'then': ('then', 'ADV'), 'them': ('they', 'PRON'), 'would': ('would', 'AUX'), 'write': ('write', 'VERB'), 'written': ('written', 'VERB'), 'wrote': ('wrote', 'VERB'), 'like': ('like', 'INTJ'), 'so': ('so', 'ADV'), 'these': ('these', 'DET'), 'her': ('her', 'PRON'), 'long': ('long', 'ADJ'), 'make': ('make', 'VERB'), 'thing': ('thing', 'NOUN'), 'see': ('see', 'VERB'), 'him': ('he', 'PRON'), 'two': ('two', 'NUM'), 'has': ('have', 'AUX'), 'look': ('look', 'VERB'), 'more': ('more', 'ADV'), 'day': ('day', 'NOUN'), 'could': ('could', 'AUX'), 'go': ('go', 'AUX'), 'come': ('come', 'NOUN'), 'did': ('do', 'AUX'), 'my': ('my', 'PRON'), 'sound': ('sound', 'NOUN'), 'no': ('no', 'DET'), 'most': ('most', 'ADJ'), 'number': ('number', 'NOUN'), 'who': ('who', 'SCONJ'), 'Who': ('who', 'SCONJ'),'over': ('over', 'ADV'), 'know': ('know', 'VERB'), 'water': ('water', 'NOUN'), 'than': ('than', 'ADP'), 'call': ('call', 'VERB'), 'first': ('first', 'ADJ'), 'people': ('people', 'NOUN'), 'may': ('may', 'AUX'), 'down': ('down', 'ADP'), 'side': ('side', 'NOUN'), 'been': ('be', 'AUX'), 'now': ('now', 'ADV'), 'find': ('find', 'VERB'), 'any': ('any', 'DET'), 'new': ('new', 'ADJ'), 'work': ('work', 'NOUN'), 'part': ('part', 'NOUN'), 'take': ('take', 'VERB'), 'get': ('get', 'NOUN'), 'place': ('place', 'NOUN'), 'made': ('make', 'VERB'), 'live': ('live', 'VERB'), 'where': ('where', 'SCONJ'), 'after': ('after', 'ADP'), 'back': ('back', 'ADV'), 'little': ('little', 'ADJ'), 'only': ('only', 'ADV'), 'round': ('round', 'ADJ'), 'man': ('man', 'NOUN'), 'year': ('year', 'NOUN'), 'came': ('come', 'VERB'), 'show': ('show', 'NOUN'), 'every': ('every', 'DET'), 'good': ('good', 'ADJ'), 'me': ('I', 'PRON'), 'give': ('give', 'VERB'), 'Give': ('Give', 'VERB'), 'our': ('our', 'PRON'), 'under': ('under', 'ADP'), 'name': ('name', 'NOUN'), 'very': ('very', 'ADV'), 'through': ('through', 'ADP'), 'just': ('just', 'ADV'), 'form': ('form', 'VERB'), 'much': ('much', 'ADJ'), 'great': ('great', 'ADJ'), 'think': ('think', 'NOUN'), 'say': ('say', 'VERB'), 'help': ('help', 'VERB'), 'low': ('low', 'ADJ'), 'line': ('line', 'NOUN'), 'before': ('before', 'SCONJ'), 'turn': ('turn', 'NOUN'), 'cause': ('cause', 'NOUN'), 'same': ('same', 'ADJ'), 'mean': ('mean', 'NOUN'), 'differ': ('differ', 'VERB'), 'move': ('move', 'NOUN'), 'right': ('right', 'ADJ'), 'boy': ('boy', 'NOUN'), 'old': ('old', 'ADJ'), 'too': ('too', 'ADV'), 'does': ('do', 'AUX'), 'tell': ('tell', 'VERB'), 'sentence': ('sentence', 'NOUN'), 'set': ('set', 'VERB'), 'three': ('three', 'NUM'), 'want': ('want', 'VERB'), 'air': ('air', 'NOUN'), 'well': ('well', 'ADV'), 'also': ('also', 'ADV'), 'play': ('play', 'VERB'), 'small': ('small', 'ADJ'), 'end': ('end', 'NOUN'), 'put': ('put', 'VERB'), 'home': ('home', 'NOUN'), 'read': ('read', 'VERB'), 'hand': ('hand', 'NOUN'), 'port': ('port', 'NOUN'), 'large': ('large', 'ADJ'), 'spell': ('spell', 'NOUN'), 'add': ('add', 'VERB'), 'even': ('even', 'ADV'), 'land': ('land', 'NOUN'), 'here': ('here', 'ADV'), 'must': ('must', 'AUX'), 'big': ('big', 'ADJ'), 'high': ('high', 'ADJ'), 'such': ('such', 'ADJ'), 'follow': ('follow', 'NOUN'), 'act': ('act', 'NOUN'), 'why': ('why', 'SCONJ'), 'Why': ('why', 'SCONJ'), 'ask': ('ask', 'VERB'), 'men': ('man', 'NOUN'), 'change': ('change', 'NOUN'), 'went': ('go', 'VERB'), 'light': ('light', 'ADJ'), 'kind': ('kind', 'NOUN'), 'off': ('off', 'ADP'), 'need': ('need', 'NOUN'), 'house': ('house', 'NOUN'), 'picture': ('picture', 'NOUN'), 'try': ('try', 'VERB'), 'us': ('we', 'PRON'), 'again': ('again', 'ADV'), 'animal': ('animal', 'NOUN'), 'point': ('point', 'NOUN'), 'mother': ('mother', 'NOUN'), 'world': ('world', 'NOUN'), 'near': ('near', 'ADP'), 'build': ('build', 'VERB'), 'self': ('self', 'NOUN'), 'earth': ('earth', 'NOUN'), 'father': ('father', 'NOUN'), 'head': ('head', 'NOUN'), 'stand': ('stand', 'VERB'), 'own': ('own', 'ADJ'), 'page': ('page', 'NOUN'), 'should': ('should', 'AUX'), 'country': ('country', 'NOUN'), 'found': ('find', 'VERB'), 'answer': ('answer', 'NOUN'), 'school': ('school', 'NOUN'), 'grow': ('grow', 'VERB'), 'study': ('study', 'NOUN'), 'still': ('still', 'ADV'), 'learn': ('learn', 'VERB'), 'plant': ('plant', 'NOUN'), 'cover': ('cover', 'VERB'), 'food': ('food', 'NOUN'), 'sun': ('sun', 'NOUN'), 'four': ('four', 'NUM'), 'thought': ('thought', 'NOUN'), 'let': ('let', 'AUX'), 'keep': ('keep', 'VERB'), 'eye': ('eye', 'NOUN'), 'never': ('never', 'ADV'), 'last': ('last', 'ADJ'), 'door': ('door', 'NOUN'), 'between': ('between', 'ADP'), 'city': ('city', 'NOUN'), 'tree': ('tree', 'NOUN'), 'cross': ('cross', 'NOUN'), 'since': ('since', 'ADV'), 'hard': ('hard', 'ADJ'), 'start': ('start', 'NOUN'), 'might': ('might', 'AUX'), 'story': ('story', 'NOUN'), 'saw': ('see', 'VERB'), 'far': ('far', 'ADV'), 'sea': ('sea', 'NOUN'), 'draw': ('draw', 'NOUN'), 'left': ('leave', 'VERB'), 'late': ('late', 'ADJ'), 'run': ('run', 'NOUN'), "n't": ('not', 'PART'), 'while': ('while', 'SCONJ'), 'press': ('press', 'NOUN'), 'close': ('close', 'ADJ'), 'night': ('night', 'NOUN'), 'real': ('real', 'ADJ'), 'life': ('life', 'NOUN'), 'few': ('few', 'ADJ'), 'stop': ('stop', 'VERB'), 'open': ('open', 'ADJ'), 'seem': ('seem', 'VERB'), 'together': ('together', 'ADV'), 'next': ('next', 'ADJ'), 'white': ('white', 'ADJ'), 'children': ('child', 'NOUN'), 'begin': ('begin', 'VERB'), 'got': ('get', 'AUX'), 'walk': ('walk', 'VERB'), 'example': ('example', 'NOUN'), 'ease': ('ease', 'NOUN'), 'paper': ('paper', 'NOUN'), 'often': ('often', 'ADV'), 'always': ('always', 'ADV'), 'music': ('music', 'NOUN'), 'those': ('those', 'DET'), 'both': ('both', 'CCONJ'), 'mark': ('mark', 'NOUN'), 'book': ('book', 'NOUN'), 'letter': ('letter', 'NOUN'), 'until': ('until', 'SCONJ'), 'mile': ('mile', 'NOUN'), 'river': ('river', 'NOUN'), 'car': ('car', 'NOUN'), 'feet': ('foot', 'NOUN'), 'care': ('care', 'NOUN'), 'second': ('second', 'ADJ'), 'group': ('group', 'NOUN'), 'carry': ('carry', 'NOUN'), 'took': ('take', 'VERB'), 'rain': ('rain', 'NOUN'), 'eat': ('eat', 'VERB'), 'room': ('room', 'NOUN'), 'friend': ('friend', 'NOUN'), 'began': ('begin', 'VERB'), 'idea': ('idea', 'NOUN'), 'fish': ('fish', 'NOUN'), 'mountain': ('mountain', 'NOUN'), 'north': ('north', 'NOUN'), 'once': ('once', 'ADV'), 'base': ('base', 'NOUN'), 'hear': ('hear', 'VERB'), 'horse': ('horse', 'NOUN'), 'cut': ('cut', 'NOUN'), 'sure': ('sure', 'ADJ'), 'watch': ('watch', 'VERB'), 'color': ('color', 'NOUN'), 'face': ('face', 'NOUN'), 'wood': ('wood', 'NOUN'), 'main': ('main', 'ADJ'), 'enough': ('enough', 'ADJ'), 'plain': ('plain', 'ADJ'), 'girl': ('girl', 'NOUN'), 'usual': ('usual', 'ADJ'), 'young': ('young', 'ADJ'), 'ready': ('ready', 'ADJ'), 'above': ('above', 'ADP'), 'ever': ('ever', 'ADV'), 'red': ('red', 'ADJ'), 'Red': ('red', 'ADJ'), 'list': ('list', 'NOUN'), 'though': ('though', 'ADV'), 'feel': ('feel', 'VERB'), 'talk': ('talk', 'NOUN'), 'bird': ('bird', 'NOUN'), 'soon': ('soon', 'ADV'), 'body': ('body', 'NOUN'), 'dog': ('dog', 'NOUN'), 'dogs': ('dog', 'NOUN'), "'s": ("'s", 'PART'), 'family': ('family', 'NOUN'), 'direct': ('direct', 'ADJ'), 'pose': ('pose', 'NOUN'), 'leave': ('leave', 'VERB'), 'song': ('song', 'NOUN'), 'measure': ('measure', 'NOUN'), 'state': ('state', 'NOUN'), 'product': ('product', 'NOUN'), 'black': ('black', 'ADJ'), 'short': ('short', 'ADJ'), 'numeral': ('numeral', 'ADJ'), 'class': ('class', 'NOUN'), 'wind': ('wind', 'NOUN'), 'question': ('question', 'NOUN'), 'happen': ('happen', 'VERB'), 'complete': ('complete', 'ADJ'), 'ship': ('ship', 'NOUN'), 'area': ('area', 'NOUN'), 'half': ('half', 'ADJ'), 'rock': ('rock', 'NOUN'), 'order': ('order', 'NOUN'), 'fire': ('fire', 'NOUN'), 'south': ('south', 'ADJ'), 'problem': ('problem', 'NOUN'), 'piece': ('piece', 'NOUN'), 'told': ('tell', 'VERB'), 'knew': ('know', 'VERB'), 'pass': ('pass', 'VERB'), 'farm': ('farm', 'NOUN'), 'top': ('top', 'ADJ'), 'whole': ('whole', 'ADJ'), 'king': ('king', 'NOUN'), 'size': ('size', 'NOUN'), 'heard': ('hear', 'VERB'), 'best': ('good', 'ADJ'), 'hour': ('hour', 'NOUN'), 'better': ('well', 'ADJ'), 'true': ('true', 'ADJ'), 'during': ('during', 'ADP'), 'hundred': ('hundred', 'NUM'), 'am': ('be', 'AUX'), 'remember': ('remember', 'VERB'), 'step': ('step', 'NOUN'), 'early': ('early', 'ADJ'), 'hold': ('hold', 'VERB'), 'west': ('west', 'NOUN'), 'ground': ('ground', 'NOUN'), 'interest': ('interest', 'NOUN'), 'reach': ('reach', 'VERB'), 'fast': ('fast', 'ADJ'), 'five': ('five', 'NUM'), 'sing': ('sing', 'NOUN'), 'sings': ('sing', 'NOUN'), 'listen': ('listen', 'VERB'), 'six': ('six', 'NUM'), 'table': ('table', 'NOUN'), 'travel': ('travel', 'NOUN'), 'less': ('less', 'ADJ'), 'morning': ('morning', 'NOUN'), 'ten': ('ten', 'NUM'), 'simple': ('simple', 'ADJ'), 'several': ('several', 'ADJ'), 'vowel': ('vowel', 'NOUN'), 'toward': ('toward', 'ADP'), 'war': ('war', 'NOUN'), 'lay': ('lie', 'VERB'), 'against': ('against', 'ADP'), 'pattern': ('pattern', 'NOUN'), 'slow': ('slow', 'ADJ'), 'center': ('center', 'NOUN'), 'love': ('love', 'NOUN'), 'person': ('person', 'NOUN'), 'money': ('money', 'NOUN'), 'serve': ('serve', 'VERB'), 'appear': ('appear', 'VERB'), 'road': ('road', 'NOUN'), 'map': ('map', 'NOUN'), 'science': ('science', 'NOUN'), 'rule': ('rule', 'NOUN'), 'govern': ('govern', 'NOUN'), 'pull': ('pull', 'VERB'), 'cold': ('cold', 'ADJ'), 'notice': ('notice', 'NOUN'), 'voice': ('voice', 'NOUN'), 'fall': ('fall', 'NOUN'), 'power': ('power', 'NOUN'), 'town': ('town', 'NOUN'), 'fine': ('fine', 'ADJ'), 'certain': ('certain', 'ADJ'), 'fly': ('fly', 'NOUN'), 'unit': ('unit', 'NOUN'), 'lead': ('lead', 'VERB'), 'cry': ('cry', 'NOUN'), 'dark': ('dark', 'ADJ'), 'machine': ('machine', 'NOUN'), 'note': ('note', 'NOUN'), 'wait': ('wait', 'VERB'), 'plan': ('plan', 'NOUN'), 'figure': ('figure', 'NOUN'), 'star': ('star', 'NOUN'), 'box': ('box', 'NOUN'), 'noun': ('noun', 'NOUN'), 'field': ('field', 'NOUN'), 'rest': ('rest', 'NOUN'), 'correct': ('correct', 'ADJ'), 'able': ('able', 'ADJ'), 'pound': ('pound', 'NOUN'), 'done': ('do', 'VERB'), 'beauty': ('beauty', 'NOUN'), 'drive': ('drive', 'NOUN'), 'stood': ('stand', 'VERB'), 'contain': ('contain', 'VERB'), 'front': ('front', 'ADJ'), 'teach': ('teach', 'NOUN'), 'week': ('week', 'NOUN'), 'final': ('final', 'ADJ'), 'gave': ('give', 'VERB'), 'green': ('green', 'ADJ'), 'oh': ('oh', 'ADJ'), 'quick': ('quick', 'ADJ'), 'develop': ('develop', 'VERB'), 'sleep': ('sleep', 'NOUN'), 'warm': ('warm', 'ADJ'), 'free': ('free', 'ADJ'), 'minute': ('minute', 'NOUN'), 'strong': ('strong', 'ADJ'), 'special': ('special', 'ADJ'), 'mind': ('mind', 'NOUN'), 'behind': ('behind', 'ADP'), 'clear': ('clear', 'ADJ'), 'tail': ('tail', 'NOUN'), 'produce': ('produce', 'NOUN'), 'fact': ('fact', 'NOUN'), 'street': ('street', 'NOUN'), 'inch': ('inch', 'NOUN'), 'lot': ('lot', 'NOUN'), 'nothing': ('nothing', 'PRON'), 'course': ('course', 'NOUN'), 'stay': ('stay', 'VERB'), 'wheel': ('wheel', 'NOUN'), 'full': ('full', 'ADJ'), 'force': ('force', 'NOUN'), 'blue': ('blue', 'ADJ'), 'object': ('object', 'NOUN'), 'decide': ('decide', 'VERB'), 'surface': ('surface', 'NOUN'), 'deep': ('deep', 'ADJ'), 'moon': ('moon', 'NOUN'), 'island': ('island', 'NOUN'), 'foot': ('foot', 'NOUN'), 'yet': ('yet', 'ADV'), 'busy': ('busy', 'ADJ'), 'test': ('test', 'NOUN'), 'record': ('record', 'NOUN'), 'boat': ('boat', 'NOUN'), 'common': ('common', 'ADJ'), 'gold': ('gold', 'NOUN'), 'possible': ('possible', 'ADJ'), 'plane': ('plane', 'NOUN'), 'age': ('age', 'NOUN'), 'dry': ('dry', 'ADJ'), 'wonder': ('wonder', 'NOUN'), 'laugh': ('laugh', 'NOUN'), 'thousand': ('thousand', 'NUM'), 'ago': ('ago', 'ADP'), 'ran': ('run', 'VERB'), 'check': ('check', 'NOUN'), 'game': ('game', 'NOUN'), 'shape': ('shape', 'NOUN'), 'yes': ('yes', 'INTJ'), 'cool': ('cool', 'ADJ'), 'miss': ('miss', 'NOUN'), 'brought': ('bring', 'VERB'), 'heat': ('heat', 'NOUN'), 'snow': ('snow', 'NOUN'), 'bed': ('bed', 'NOUN'), 'bring': ('bring', 'VERB'), 'sit': ('sit', 'VERB'), 'perhaps': ('perhaps', 'ADV'), 'fill': ('fill', 'VERB'), 'east': ('east', 'NOUN'), 'weight': ('weight', 'NOUN'), 'language': ('language', 'NOUN'), 'among': ('among', 'ADP'), 'adult': ('adult', 'NOUN'), 'adults': ('adult', 'NOUN')}



class SentenceReadingAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, sentence, question):
    
        '''
          You can use a library like spacy (https://spacy.io/usage/linguistic-features) to preprocess the
            mostcommon.txt file. There are others that could be used but you must use them in preprocessing only.
            You CANNOT import the library into Gradescope.
          
          You must include whatever preprocessing you've done into your SentenceReadingAgent.py.
          
          DO NOT use another file .txt or .csv. Hard code your DICTS | LISTS into this .py file
          
          While the supplied mostcommon.txt contains most of the common words you will need
            you can (and SHOULD) expand the file as you find cases that the agent has problems
            processing. 
            
          Also not all words will be processed using the correct lexing for every possible problem the 
            agent might encounter and you are ENCOURAGED to expand these in your agents knowledge representation.
        '''
    
        #Add your code here! Your solve method should receive
		#two strings as input: sentence and question. It should
		#return a string representing the answer to the question.

        original_sentence = sentence
        for c in string.punctuation:
            sentence = sentence.replace(c, "")
            words_in_sentence = sentence.split(" ")

        for c in string.punctuation:
            question = question.replace(c, "")
            words_in_question = question.split(" ")



        # dict of pos and list of words from the sentence
        pos_dict_sentence = {}
        for w in words_in_sentence:
            pos_w = LEMMA_DICT[w][1] if w in LEMMA_DICT else 'SPECIAL'
            if pos_w in pos_dict_sentence:
                pos_dict_sentence[pos_w].append(w)
            else:
                pos_dict_sentence[pos_w] = [w]

        # dict of pos and list of words from the question
        pos_dict_question = {}
        for w in words_in_question:
            pos_w = LEMMA_DICT[w][1] if w in LEMMA_DICT else 'SPECIAL'
            if pos_w in pos_dict_question:
                pos_dict_question[pos_w].append(w)
            else:
                pos_dict_question[pos_w] = [w]


        # heuristics
        # time
        if 'time' in words_in_question:
            for w in original_sentence.split():
                if ':' in w:
                    return w
        # when
        elif 'When' in words_in_question:

            # case:
            # Sentence: Serena ran a mile this morning.
            # Question: When did Serena run?
            # Answer: morning
            activation_words = ['morning', 'afternoon', 'evening', 'night', 'day', 'week', 'month', 'year']
            for w in words_in_sentence:
                if w in activation_words:
                    return w

            # case:
            # Sentence: It will snow soon.
            # Question: When will it snow?
            # Answer: soon
            for w in words_in_sentence:
                if LEMMA_DICT[w][1] == 'ADV':
                    return w
        # where
        elif 'Where' in words_in_question:
            activation = ['go', 'walk', 'in', 'from', 'to']
            for a in activation:
                if a in words_in_sentence:
                    if 'other' not in words_in_sentence:
                        w = words_in_sentence[ words_in_sentence.index(a) + 2 ]
                    else:
                        w = words_in_sentence[ words_in_sentence.index('other') + 3 ]
                    return w
            else:
                l = [n for n in pos_dict_sentence['NOUN'] if n not in words_in_question]
                w = l[0] if len(l) > 0 else None
                return w
        # who
        elif 'Who' in words_in_question:
            # case:
            # when there no propn in the question, return the first propn in the sentence
            if 'PROPN' not in [LEMMA_DICT[w][1] for w in words_in_question]:
                for w in words_in_sentence:
                    if LEMMA_DICT[w][1] == 'PROPN':
                        return w
            # case:
            #          "David and Lucy walk one mile to go to school every day at 8:00AM when there is no snow."
            # when there is a propn in the question, return the other propn in the sentence
            elif 'PROPN' in [LEMMA_DICT[w][1] for w in words_in_question]:
                for w in words_in_sentence:
                    if LEMMA_DICT[w][1] == 'PROPN' and  w not in words_in_question:
                        return w
        # what
        elif 'What' in words_in_question:
            if 'color' in words_in_question:
                w = pos_dict_sentence['ADJ'][0]
                return w
            else:
                if pos_dict_sentence.get('NOUN', None) is not None:
                    l = [n for n in pos_dict_sentence['NOUN'] if n not in words_in_question]
                    w = l[0] if len(l) > 0 else None
                return w

        elif 'How' in words_in_question:
            # case: how far, how long
            description = words_in_question[1] # far, long, many, much
            if description in ['far', 'long']:
                if 'mile' in words_in_sentence:
                    w = 'mile'
                    return w
                elif LEMMA_DICT[description][1] == 'ADJ':
                    w = pos_dict_sentence['ADJ'][-1] if pos_dict_sentence.get('ADJ', None) is not None else None
                    return w
            elif 'many' in words_in_question:
                if pos_dict_sentence.get('NUM', None) is not None:
                    w = pos_dict_sentence['NUM'][0]
                return w
            elif 'much' in words_in_question:
                if pos_dict_sentence.get('DET', None) is not None:
                    w = pos_dict_sentence['DET'][0]
                if pos_dict_sentence.get('ADV', None) is not None:
                    w = pos_dict_sentence['ADV'][0]
                return w
            elif LEMMA_DICT[description][1] == 'ADJ':
                w = pos_dict_sentence['ADJ'][-1] if pos_dict_sentence.get('ADJ', None) is not None else None
                return w
            elif 'do' in words_in_question: # how do
                if pos_dict_sentence.get('VERB', None) is not None:
                    w = pos_dict_sentence['VERB'][0]
                return w

            return None

        return None

if __name__ == "__main__":
    test_agent = SentenceReadingAgent()

    sentence_1 = "The island is east of the city."
    question_1 = "Where is the island?"
    question_2 = "What did Ada bring?"
    question_3 = "Who did Ada bring the note to?"
    question_4 = "How long was the note?"

    sentence_2 = "David and Lucy walk one mile to go to school every day at 8:00AM when there is no snow."
    question_5 = "Who does Lucy go to school with?"
    question_6 = "Where do David and Lucy go?"
    question_7 = "How far do David and Lucy walk?"
    question_8 = "How do David and Lucy get to school?"
    question_9 = "At what time do David and Lucy walk to school?"

    print(test_agent.solve(sentence_1, question_1))  # "Ada"
    # print(test_agent.solve(sentence_1, question_2))  # "note" or "a note"
    # print(test_agent.solve(sentence_1, question_3))  # "Irene"
    # print(test_agent.solve(sentence_1, question_4))  # "short"
    #
    # print(test_agent.solve(sentence_2, question_5))  # "David"
    # print(test_agent.solve(sentence_2, question_6))  # "school"
    # print(test_agent.solve(sentence_2, question_7))  # "mile" or "a mile"
    # print(test_agent.solve(sentence_2, question_8))  # "walk"
    # print(test_agent.solve(sentence_2, question_9))  # "8:00AM"
