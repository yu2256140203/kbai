import re
import string

DEBUG = 1
LEMMA_DICT = \
{'Serena': ('Serena', 'PROPN'), '\n': ('\n', 'SPACE'), 'Andrew': ('Andrew', 'PROPN'), 'Bobbie': ('Bobbie', 'PROPN'), 'Cason': ('Cason', 'PROPN'), 'David': ('David', 'PROPN'), 'Farzana': ('Farzana', 'PROPN'), 'Frank': ('Frank', 'PROPN'), 'Hannah': ('Hannah', 'PROPN'), 'Ida': ('Ida', 'PROPN'), 'Irene': ('Irene', 'PROPN'), 'Jim': ('Jim', 'PROPN'), 'Jose': ('Jose', 'PROPN'), 'Keith': ('Keith', 'PROPN'), 'Laura': ('Laura', 'PROPN'), 'Lucy': ('Lucy', 'PROPN'), 'Meredith': ('Meredith', 'PROPN'), 'Nick': ('Nick', 'PROPN'), 'Ada': ('Ada', 'PROPN'), 'Yeeling': ('Yeeling', 'PROPN'), 'Yan': ('Yan', 'PROPN'), 'the': ('the', 'PRON'), 'of': ('of', 'ADP'), 'to': ('to', 'ADP'), 'and': ('and', 'CCONJ'), 'a': ('a', 'PRON'), 'in': ('in', 'ADP'), 'is': ('be', 'AUX'), 'it': ('it', 'PRON'), 'you': ('you', 'PRON'), 'that': ('that', 'SCONJ'), 'he': ('he', 'PRON'), 'was': ('be', 'AUX'), 'for': ('for', 'ADP'), 'on': ('on', 'ADP'), 'are': ('be', 'AUX'), 'with': ('with', 'ADP'), 'as': ('as', 'ADP'), 'I': ('I', 'PRON'), 'his': ('his', 'PRON'), 'they': ('they', 'PRON'), 'be': ('be', 'VERB'), 'at': ('at', 'ADP'), 'one': ('one', 'NUM'), 'have': ('have', 'VERB'), 'this': ('this', 'PRON'), 'from': ('from', 'ADP'), 'or': ('or', 'CCONJ'), 'had': ('have', 'VERB'), 'by': ('by', 'ADP'), 'hot': ('hot', 'ADJ'), 'but': ('but', 'CCONJ'), 'some': ('some', 'DET'), 'what': ('what', 'SCONJ'), 'What': ('what', 'SCONJ'),'there': ('there', 'PRON'), 'we': ('we', 'PRON'), 'can': ('can', 'AUX'), 'out': ('out', 'ADP'), 'other': ('other', 'ADJ'), 'were': ('be', 'AUX'), 'all': ('all', 'ADV'), 'your': ('your', 'PRON'), 'when': ('when', 'SCONJ'), 'When': ('when', 'SCONJ'), 'up': ('up', 'NOUN'), 'use': ('use', 'VERB'), 'word': ('word', 'NOUN'), 'how': ('how', 'SCONJ'), 'How': ('how', 'SCONJ'), 'said': ('say', 'VERB'), 'an': ('an', 'DET'), 'each': ('each', 'DET'), 'she': ('she', 'PRON'), 'which': ('which', 'PRON'), 'do': ('do', 'AUX'), 'their': ('their', 'PRON'), 'time': ('time', 'NOUN'), 'if': ('if', 'SCONJ'), 'will': ('will', 'AUX'), 'way': ('way', 'NOUN'), 'about': ('about', 'ADV'), 'many': ('many', 'ADJ'), 'then': ('then', 'ADV'), 'them': ('they', 'PRON'), 'would': ('would', 'AUX'), 'write': ('write', 'VERB'), 'wrote': ('write', 'VERB'), 'like': ('like', 'INTJ'), 'so': ('so', 'ADV'), 'these': ('these', 'DET'), 'her': ('her', 'PRON'), 'long': ('long', 'ADJ'), 'make': ('make', 'VERB'), 'thing': ('thing', 'NOUN'), 'see': ('see', 'VERB'), 'him': ('he', 'PRON'), 'two': ('two', 'NUM'), 'has': ('have', 'AUX'), 'look': ('look', 'VERB'), 'more': ('more', 'ADV'), 'day': ('day', 'NOUN'), 'could': ('could', 'AUX'), 'go': ('go', 'AUX'), 'come': ('come', 'NOUN'), 'did': ('do', 'AUX'), 'my': ('my', 'PRON'), 'sound': ('sound', 'NOUN'), 'no': ('no', 'DET'), 'most': ('most', 'ADJ'), 'number': ('number', 'NOUN'), 'who': ('who', 'SCONJ'), 'Who': ('who', 'SCONJ'),'over': ('over', 'ADV'), 'know': ('know', 'VERB'), 'water': ('water', 'NOUN'), 'than': ('than', 'ADP'), 'call': ('call', 'VERB'), 'first': ('first', 'ADJ'), 'people': ('people', 'NOUN'), 'may': ('may', 'AUX'), 'down': ('down', 'ADP'), 'side': ('side', 'NOUN'), 'been': ('be', 'AUX'), 'now': ('now', 'ADV'), 'find': ('find', 'VERB'), 'any': ('any', 'DET'), 'new': ('new', 'ADJ'), 'work': ('work', 'NOUN'), 'part': ('part', 'NOUN'), 'take': ('take', 'VERB'), 'get': ('get', 'NOUN'), 'place': ('place', 'NOUN'), 'made': ('make', 'VERB'), 'live': ('live', 'VERB'), 'where': ('where', 'SCONJ'), 'after': ('after', 'ADP'), 'back': ('back', 'ADV'), 'little': ('little', 'ADJ'), 'only': ('only', 'ADV'), 'round': ('round', 'ADJ'), 'man': ('man', 'NOUN'), 'year': ('year', 'NOUN'), 'came': ('come', 'VERB'), 'show': ('show', 'NOUN'), 'every': ('every', 'DET'), 'good': ('good', 'ADJ'), 'me': ('I', 'PRON'), 'give': ('give', 'VERB'), 'our': ('our', 'PRON'), 'under': ('under', 'ADP'), 'name': ('name', 'NOUN'), 'very': ('very', 'ADV'), 'through': ('through', 'ADP'), 'just': ('just', 'ADV'), 'form': ('form', 'VERB'), 'much': ('much', 'ADJ'), 'great': ('great', 'ADJ'), 'think': ('think', 'NOUN'), 'say': ('say', 'VERB'), 'help': ('help', 'VERB'), 'low': ('low', 'ADJ'), 'line': ('line', 'NOUN'), 'before': ('before', 'SCONJ'), 'turn': ('turn', 'NOUN'), 'cause': ('cause', 'NOUN'), 'same': ('same', 'ADJ'), 'mean': ('mean', 'NOUN'), 'differ': ('differ', 'VERB'), 'move': ('move', 'NOUN'), 'right': ('right', 'ADJ'), 'boy': ('boy', 'NOUN'), 'old': ('old', 'ADJ'), 'too': ('too', 'ADV'), 'does': ('do', 'AUX'), 'tell': ('tell', 'VERB'), 'sentence': ('sentence', 'NOUN'), 'set': ('set', 'VERB'), 'three': ('three', 'NUM'), 'want': ('want', 'VERB'), 'air': ('air', 'NOUN'), 'well': ('well', 'ADV'), 'also': ('also', 'ADV'), 'play': ('play', 'VERB'), 'small': ('small', 'ADJ'), 'end': ('end', 'NOUN'), 'put': ('put', 'VERB'), 'home': ('home', 'NOUN'), 'read': ('read', 'VERB'), 'hand': ('hand', 'NOUN'), 'port': ('port', 'NOUN'), 'large': ('large', 'ADJ'), 'spell': ('spell', 'NOUN'), 'add': ('add', 'VERB'), 'even': ('even', 'ADV'), 'land': ('land', 'NOUN'), 'here': ('here', 'ADV'), 'must': ('must', 'AUX'), 'big': ('big', 'ADJ'), 'high': ('high', 'ADJ'), 'such': ('such', 'ADJ'), 'follow': ('follow', 'NOUN'), 'act': ('act', 'NOUN'), 'why': ('why', 'SCONJ'), 'Why': ('why', 'SCONJ'), 'ask': ('ask', 'VERB'), 'men': ('man', 'NOUN'), 'change': ('change', 'NOUN'), 'went': ('go', 'VERB'), 'light': ('light', 'ADJ'), 'kind': ('kind', 'NOUN'), 'off': ('off', 'ADP'), 'need': ('need', 'NOUN'), 'house': ('house', 'NOUN'), 'picture': ('picture', 'NOUN'), 'try': ('try', 'VERB'), 'us': ('we', 'PRON'), 'again': ('again', 'ADV'), 'animal': ('animal', 'NOUN'), 'point': ('point', 'NOUN'), 'mother': ('mother', 'NOUN'), 'world': ('world', 'NOUN'), 'near': ('near', 'ADP'), 'build': ('build', 'VERB'), 'self': ('self', 'NOUN'), 'earth': ('earth', 'NOUN'), 'father': ('father', 'NOUN'), 'head': ('head', 'NOUN'), 'stand': ('stand', 'VERB'), 'own': ('own', 'ADJ'), 'page': ('page', 'NOUN'), 'should': ('should', 'AUX'), 'country': ('country', 'NOUN'), 'found': ('find', 'VERB'), 'answer': ('answer', 'NOUN'), 'school': ('school', 'NOUN'), 'grow': ('grow', 'VERB'), 'study': ('study', 'NOUN'), 'still': ('still', 'ADV'), 'learn': ('learn', 'VERB'), 'plant': ('plant', 'NOUN'), 'cover': ('cover', 'VERB'), 'food': ('food', 'NOUN'), 'sun': ('sun', 'NOUN'), 'four': ('four', 'NUM'), 'thought': ('thought', 'NOUN'), 'let': ('let', 'AUX'), 'keep': ('keep', 'VERB'), 'eye': ('eye', 'NOUN'), 'never': ('never', 'ADV'), 'last': ('last', 'ADJ'), 'door': ('door', 'NOUN'), 'between': ('between', 'ADP'), 'city': ('city', 'NOUN'), 'tree': ('tree', 'NOUN'), 'cross': ('cross', 'NOUN'), 'since': ('since', 'ADV'), 'hard': ('hard', 'ADJ'), 'start': ('start', 'NOUN'), 'might': ('might', 'AUX'), 'story': ('story', 'NOUN'), 'saw': ('see', 'VERB'), 'far': ('far', 'ADV'), 'sea': ('sea', 'NOUN'), 'draw': ('draw', 'NOUN'), 'left': ('leave', 'VERB'), 'late': ('late', 'ADJ'), 'run': ('run', 'NOUN'), "n't": ('not', 'PART'), 'while': ('while', 'SCONJ'), 'press': ('press', 'NOUN'), 'close': ('close', 'ADJ'), 'night': ('night', 'NOUN'), 'real': ('real', 'ADJ'), 'life': ('life', 'NOUN'), 'few': ('few', 'ADJ'), 'stop': ('stop', 'VERB'), 'open': ('open', 'ADJ'), 'seem': ('seem', 'VERB'), 'together': ('together', 'ADV'), 'next': ('next', 'ADJ'), 'white': ('white', 'ADJ'), 'children': ('child', 'NOUN'), 'begin': ('begin', 'VERB'), 'got': ('get', 'AUX'), 'walk': ('walk', 'NOUN'), 'example': ('example', 'NOUN'), 'ease': ('ease', 'NOUN'), 'paper': ('paper', 'NOUN'), 'often': ('often', 'ADV'), 'always': ('always', 'ADV'), 'music': ('music', 'NOUN'), 'those': ('those', 'DET'), 'both': ('both', 'CCONJ'), 'mark': ('mark', 'NOUN'), 'book': ('book', 'NOUN'), 'letter': ('letter', 'NOUN'), 'until': ('until', 'SCONJ'), 'mile': ('mile', 'NOUN'), 'river': ('river', 'NOUN'), 'car': ('car', 'NOUN'), 'feet': ('foot', 'NOUN'), 'care': ('care', 'NOUN'), 'second': ('second', 'ADJ'), 'group': ('group', 'NOUN'), 'carry': ('carry', 'NOUN'), 'took': ('take', 'VERB'), 'rain': ('rain', 'NOUN'), 'eat': ('eat', 'VERB'), 'room': ('room', 'NOUN'), 'friend': ('friend', 'NOUN'), 'began': ('begin', 'VERB'), 'idea': ('idea', 'NOUN'), 'fish': ('fish', 'NOUN'), 'mountain': ('mountain', 'NOUN'), 'north': ('north', 'NOUN'), 'once': ('once', 'ADV'), 'base': ('base', 'NOUN'), 'hear': ('hear', 'VERB'), 'horse': ('horse', 'NOUN'), 'cut': ('cut', 'NOUN'), 'sure': ('sure', 'ADJ'), 'watch': ('watch', 'VERB'), 'color': ('color', 'NOUN'), 'face': ('face', 'NOUN'), 'wood': ('wood', 'NOUN'), 'main': ('main', 'ADJ'), 'enough': ('enough', 'ADJ'), 'plain': ('plain', 'ADJ'), 'girl': ('girl', 'NOUN'), 'usual': ('usual', 'ADJ'), 'young': ('young', 'ADJ'), 'ready': ('ready', 'ADJ'), 'above': ('above', 'ADP'), 'ever': ('ever', 'ADV'), 'red': ('red', 'ADJ'), 'Red': ('red', 'ADJ'), 'list': ('list', 'NOUN'), 'though': ('though', 'ADV'), 'feel': ('feel', 'VERB'), 'talk': ('talk', 'NOUN'), 'bird': ('bird', 'NOUN'), 'soon': ('soon', 'ADV'), 'body': ('body', 'NOUN'), 'dog': ('dog', 'NOUN'), 'dogs': ('dog', 'NOUN'), "'s": ("'s", 'PART'), 'family': ('family', 'NOUN'), 'direct': ('direct', 'ADJ'), 'pose': ('pose', 'NOUN'), 'leave': ('leave', 'VERB'), 'song': ('song', 'NOUN'), 'measure': ('measure', 'NOUN'), 'state': ('state', 'NOUN'), 'product': ('product', 'NOUN'), 'black': ('black', 'ADJ'), 'short': ('short', 'ADJ'), 'numeral': ('numeral', 'ADJ'), 'class': ('class', 'NOUN'), 'wind': ('wind', 'NOUN'), 'question': ('question', 'NOUN'), 'happen': ('happen', 'VERB'), 'complete': ('complete', 'ADJ'), 'ship': ('ship', 'NOUN'), 'area': ('area', 'NOUN'), 'half': ('half', 'ADJ'), 'rock': ('rock', 'NOUN'), 'order': ('order', 'NOUN'), 'fire': ('fire', 'NOUN'), 'south': ('south', 'ADJ'), 'problem': ('problem', 'NOUN'), 'piece': ('piece', 'NOUN'), 'told': ('tell', 'VERB'), 'knew': ('know', 'VERB'), 'pass': ('pass', 'VERB'), 'farm': ('farm', 'NOUN'), 'top': ('top', 'ADJ'), 'whole': ('whole', 'ADJ'), 'king': ('king', 'NOUN'), 'size': ('size', 'NOUN'), 'heard': ('hear', 'VERB'), 'best': ('good', 'ADJ'), 'hour': ('hour', 'NOUN'), 'better': ('well', 'ADJ'), 'true': ('true', 'ADJ'), 'during': ('during', 'ADP'), 'hundred': ('hundred', 'NUM'), 'am': ('be', 'AUX'), 'remember': ('remember', 'VERB'), 'step': ('step', 'NOUN'), 'early': ('early', 'ADJ'), 'hold': ('hold', 'VERB'), 'west': ('west', 'NOUN'), 'ground': ('ground', 'NOUN'), 'interest': ('interest', 'NOUN'), 'reach': ('reach', 'VERB'), 'fast': ('fast', 'ADJ'), 'five': ('five', 'NUM'), 'sing': ('sing', 'NOUN'), 'sings': ('sing', 'NOUN'), 'listen': ('listen', 'VERB'), 'six': ('six', 'NUM'), 'table': ('table', 'NOUN'), 'travel': ('travel', 'NOUN'), 'less': ('less', 'ADJ'), 'morning': ('morning', 'NOUN'), 'ten': ('ten', 'NUM'), 'simple': ('simple', 'ADJ'), 'several': ('several', 'ADJ'), 'vowel': ('vowel', 'NOUN'), 'toward': ('toward', 'ADP'), 'war': ('war', 'NOUN'), 'lay': ('lie', 'VERB'), 'against': ('against', 'ADP'), 'pattern': ('pattern', 'NOUN'), 'slow': ('slow', 'ADJ'), 'center': ('center', 'NOUN'), 'love': ('love', 'NOUN'), 'person': ('person', 'NOUN'), 'money': ('money', 'NOUN'), 'serve': ('serve', 'VERB'), 'appear': ('appear', 'VERB'), 'road': ('road', 'NOUN'), 'map': ('map', 'NOUN'), 'science': ('science', 'NOUN'), 'rule': ('rule', 'NOUN'), 'govern': ('govern', 'NOUN'), 'pull': ('pull', 'VERB'), 'cold': ('cold', 'ADJ'), 'notice': ('notice', 'NOUN'), 'voice': ('voice', 'NOUN'), 'fall': ('fall', 'NOUN'), 'power': ('power', 'NOUN'), 'town': ('town', 'NOUN'), 'fine': ('fine', 'ADJ'), 'certain': ('certain', 'ADJ'), 'fly': ('fly', 'NOUN'), 'unit': ('unit', 'NOUN'), 'lead': ('lead', 'VERB'), 'cry': ('cry', 'NOUN'), 'dark': ('dark', 'ADJ'), 'machine': ('machine', 'NOUN'), 'note': ('note', 'NOUN'), 'wait': ('wait', 'VERB'), 'plan': ('plan', 'NOUN'), 'figure': ('figure', 'NOUN'), 'star': ('star', 'NOUN'), 'box': ('box', 'NOUN'), 'noun': ('noun', 'NOUN'), 'field': ('field', 'NOUN'), 'rest': ('rest', 'NOUN'), 'correct': ('correct', 'ADJ'), 'able': ('able', 'ADJ'), 'pound': ('pound', 'NOUN'), 'done': ('do', 'VERB'), 'beauty': ('beauty', 'NOUN'), 'drive': ('drive', 'NOUN'), 'stood': ('stand', 'VERB'), 'contain': ('contain', 'VERB'), 'front': ('front', 'ADJ'), 'teach': ('teach', 'NOUN'), 'week': ('week', 'NOUN'), 'final': ('final', 'ADJ'), 'gave': ('give', 'VERB'), 'green': ('green', 'ADJ'), 'oh': ('oh', 'ADJ'), 'quick': ('quick', 'ADJ'), 'develop': ('develop', 'VERB'), 'sleep': ('sleep', 'NOUN'), 'warm': ('warm', 'ADJ'), 'free': ('free', 'ADJ'), 'minute': ('minute', 'NOUN'), 'strong': ('strong', 'ADJ'), 'special': ('special', 'ADJ'), 'mind': ('mind', 'NOUN'), 'behind': ('behind', 'ADP'), 'clear': ('clear', 'ADJ'), 'tail': ('tail', 'NOUN'), 'produce': ('produce', 'NOUN'), 'fact': ('fact', 'NOUN'), 'street': ('street', 'NOUN'), 'inch': ('inch', 'NOUN'), 'lot': ('lot', 'NOUN'), 'nothing': ('nothing', 'PRON'), 'course': ('course', 'NOUN'), 'stay': ('stay', 'VERB'), 'wheel': ('wheel', 'NOUN'), 'full': ('full', 'ADJ'), 'force': ('force', 'NOUN'), 'blue': ('blue', 'ADJ'), 'object': ('object', 'NOUN'), 'decide': ('decide', 'VERB'), 'surface': ('surface', 'NOUN'), 'deep': ('deep', 'ADJ'), 'moon': ('moon', 'NOUN'), 'island': ('island', 'NOUN'), 'foot': ('foot', 'NOUN'), 'yet': ('yet', 'ADV'), 'busy': ('busy', 'ADJ'), 'test': ('test', 'NOUN'), 'record': ('record', 'NOUN'), 'boat': ('boat', 'NOUN'), 'common': ('common', 'ADJ'), 'gold': ('gold', 'NOUN'), 'possible': ('possible', 'ADJ'), 'plane': ('plane', 'NOUN'), 'age': ('age', 'NOUN'), 'dry': ('dry', 'ADJ'), 'wonder': ('wonder', 'NOUN'), 'laugh': ('laugh', 'NOUN'), 'thousand': ('thousand', 'NUM'), 'ago': ('ago', 'ADP'), 'ran': ('run', 'VERB'), 'check': ('check', 'NOUN'), 'game': ('game', 'NOUN'), 'shape': ('shape', 'NOUN'), 'yes': ('yes', 'INTJ'), 'cool': ('cool', 'ADJ'), 'miss': ('miss', 'NOUN'), 'brought': ('bring', 'VERB'), 'heat': ('heat', 'NOUN'), 'snow': ('snow', 'NOUN'), 'bed': ('bed', 'NOUN'), 'bring': ('bring', 'VERB'), 'sit': ('sit', 'VERB'), 'perhaps': ('perhaps', 'ADV'), 'fill': ('fill', 'VERB'), 'east': ('east', 'NOUN'), 'weight': ('weight', 'NOUN'), 'language': ('language', 'NOUN'), 'among': ('among', 'ADP'), 'adult': ('adult', 'NOUN'), 'adults': ('adult', 'NOUN')}


class Token:
    def __init__(self, text):
        self.text = text
        self.lemma, self.pos = LEMMA_DICT[text] if text in LEMMA_DICT else (text, 'SPECIAL')

# Thematic Role Frame
class Frame:
    def __init__(self, sentence):
        for c in sentence.split():
            if c in string.punctuation:
                sentence = sentence.replace(c, '')

        self.sentence = sentence
        self.tokens = [Token(token) for token in sentence.split()]

    def print(self):
        print('Frame type:',type(self).__name__)
        for attribute, value in self.__dict__.items():
            if value and isinstance(value, Token):
                print(f"{attribute}: {value.text}")
        print('\n')

class SentenceFrame(Frame):
    def __init__(self, sentence):
        super().__init__(sentence)

        self.verb = None
        self.agent = None
        self.object = None # default structure: SVO

        for i, token in enumerate(self.tokens):
            if token.pos == 'VERB' and not self.verb:
                self.verb = token

            elif token.pos == 'PROPN':
                if not self.agent:
                    self.agent = token

            elif token.pos == 'NOUN':
                self.object = token

            elif token.pos == 'ADP' and i < len(self.tokens) - 1 and self.tokens[i + 1].pos in ['NOUN', 'PROPN']:
                next_token = self.tokens[i + 1]
                if token.lemma == 'to':
                    self.destination = next_token
                elif token.lemma == 'from':
                    self.source = next_token
                elif token.lemma == 'at':
                    self.time = next_token
                elif token.lemma == 'for':
                    self.duration = next_token
                elif token.lemma == 'with':
                    self.instrument = next_token
                elif token.lemma == 'by':
                    self.conveyance = next_token

            elif token.pos == 'NUM' and i < len(self.tokens) - 1:
                nexttoken = self.tokens[i + 1]
                if nexttoken.lemma in ['mile', 'feet']:
                    self.distance = nexttoken
                elif nexttoken.lemma in ['minute', 'hour', 'day', 'week', 'month', 'year']:
                    self.duration = nexttoken

                # elif token.pos == 'SCONJ':
                #     self.condition = token
    def less(self, frame_b):
        res = [getattr(self, attribute).text for attribute in self.__dict__.keys() if getattr(self, attribute) and not hasattr(frame_b, attribute) ]
        if len(res) != 1:
            raise Exception(f"Error: {res}\t Difference between frames is not 1.")
        return res[0]

class QuestionFrame(Frame):
    def __init__(self, question):
        super().__init__(question)

        self.askattribute = None

        for i, token in enumerate(self.tokens):
            if token.pos == 'SCONJ':
                if self.tokens[-1].pos in ['ADP',]:
                    lasttoken = self.tokens[-1]
                    if lasttoken.text == 'to':
                        self.askattribute = 'destination'
                    elif lasttoken.text == 'from':
                        self.askattribute = 'source'
                    elif lasttoken.text == 'at':
                        self.askattribute = 'time'
                    elif lasttoken.text == 'for':
                        self.askattribute = 'duration'
                    elif lasttoken.text == 'with':
                        self.askattribute = 'instrument'
                    elif lasttoken.text == 'by':
                        self.askattribute = 'conveyance'
                elif token.lemma == 'who':
                    self.askattribute = 'agent'
                elif token.lemma == 'what':
                    self.askattribute = 'object'
                elif token.lemma == 'where':
                    self.askattribute = 'destination'
                elif token.lemma == 'when':
                    self.askattribute = 'time'
                elif token.lemma == 'how':
                    nexttoken = self.tokens[i + 1]
                    if nexttoken.text == 'long': # how long
                        self.askattribute = 'duration'
                    elif nexttoken.text == 'far': # how far
                        self.askattribute = 'distance'
        if not self.askattribute:
            raise Exception(f"Error building the question frame: {question}\n")




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

        sentence_frame = Frame(sentence)
        sentence_frame.print() if DEBUG else None

        question_frame = QuestionFrame(question)
        question_frame.print() if DEBUG else None
        print('Question asks for attribute:', question_frame.askattribute) if DEBUG else None

        # find answer from sentence_frame
        res = getattr(sentence_frame, question_frame.askattribute).text

        return res

if __name__ == "__main__":
    test_agent = SentenceReadingAgent()

    sentence_1 = "Ada brought a short note to Irene."
    question_1 = "Who brought the note?"
    question_2 = "What did Ada bring?"
    question_3 = "Who did Ada bring the note to?"
    question_4 = "How long was the note?"

    sentence_2 = "David and Lucy walk one mile to go to school every day at 8:00AM when there is no snow."
    question_5 = "Who does Lucy go to school with?"
    question_6 = "Where do David and Lucy go?"
    question_7 = "How far do David and Lucy walk?"
    question_8 = "How do David and Lucy get to school?"
    question_9 = "At what time do David and Lucy walk to school?"

    # print(test_agent.solve(sentence_1, question_1))  # "Ada"
    # print(test_agent.solve(sentence_1, question_2))  # "note" or "a note"
    # print(test_agent.solve(sentence_1, question_3))  # "Irene"
    # print(test_agent.solve(sentence_1, question_4))  # "short"
    #
    # print(test_agent.solve(sentence_2, question_5))  # "David"
    # print(test_agent.solve(sentence_2, question_6))  # "school"
    print(test_agent.solve(sentence_2, question_7))  # "mile" or "a mile"
    # print(test_agent.solve(sentence_2, question_8))  # "walk"
    # print(test_agent.solve(sentence_2, question_9))  # "8:00AM"