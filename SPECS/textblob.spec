%define name textblob
%define version 0.8.0
%define unmangled_version 0.8.0
%define unmangled_version 0.8.0
%define release 1

Summary: Simple, Pythonic text processing. Sentiment analysis, POS tagging, noun phrase parsing, and more.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: BSD

Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Steven Loria <sloria1@gmail.com>
Url: https://github.com/sloria/TextBlob

%description

TextBlob: Simplified Text Processing
====================================

.. image:: https://badge.fury.io/py/textblob.png
    :target: http://badge.fury.io/py/textblob
    :alt: Latest version

.. image:: https://travis-ci.org/sloria/TextBlob.png?branch=master
    :target: https://travis-ci.org/sloria/TextBlob
    :alt: Travis-CI

.. image:: https://pypip.in/d/textblob/badge.png
    :target: https://crate.io/packages/textblob/
    :alt: Number of PyPI downloads

.. image:: https://badge.waffle.io/sloria/TextBlob.png?label=Ready
     :target: https://waffle.io/sloria/TextBlob
     :alt: Issues in Ready


Homepage: `https://textblob.readthedocs.org/ <https://textblob.readthedocs.org/>`_

`TextBlob` is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.


.. code-block:: python

    from textblob import TextBlob

    text = '''
    The titular threat of The Blob has always struck me as the ultimate movie
    monster: an insatiably hungry, amoeba-like mass able to penetrate
    virtually any safeguard, capable of--as a doomed doctor chillingly
    describes it--"assimilating flesh on contact.
    Snide comparisons to gelatin be damned, it's a concept with the most
    devastating of potential consequences, not unlike the grey goo scenario
    proposed by technological theorists fearful of
    artificial intelligence run rampant.
    '''

    blob = TextBlob(text)
    blob.tags           # [(u'The', u'DT'), (u'titular', u'JJ'),
                        #  (u'threat', u'NN'), (u'of', u'IN'), ...]

    blob.noun_phrases   # WordList(['titular threat', 'blob',
                        #            'ultimate movie monster',
                        #            'amoeba-like mass', ...])

    for sentence in blob.sentences:
        print(sentence.sentiment)  # returns (polarity, subjectivity)
    # (0.060, 0.605)
    # (-0.341, 0.767)

    blob.translate(to="es")  # 'La amenaza titular de The Blob...'

TextBlob stands on the giant shoulders of `NLTK`_ and `pattern`_, and plays nicely with both.

Features
--------

- Noun phrase extraction
- Part-of-speech tagging
- Sentiment analysis
- Classification (Naive Bayes, Decision Tree)
- Language translation and detection powered by Google Translate
- Tokenization (splitting text into words and sentences)
- Word and phrase frequencies
- Parsing
- `n`-grams
- Word inflection (pluralization and singularization) and lemmatization
- Spelling correction
- JSON serialization
- Add new models or languages through extensions
- WordNet integration

Get it now
----------
::

    $ pip install -U textblob
    $ curl https://raw.github.com/sloria/TextBlob/master/download_corpora.py | python

Examples
--------

See more examples at the `Quickstart guide`_.

.. _`Quickstart guide`: https://textblob.readthedocs.org/en/latest/quickstart.html#quickstart


Documentation
-------------

Full documentation is available at https://textblob.readthedocs.org/.

Requirements
------------

- Python >= 2.6 or >= 3.3


License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/sloria/TextBlob/blob/master/LICENSE>`_ file for more details.

.. _pattern: http://www.clips.ua.ac.be/pattern
.. _NLTK: http://nltk.org/


Changelog
=========

0.8.0 (2013-10-23)
------------------
- *Backwards-incompatible*: Renamed package to ``textblob``. This avoids clashes with other namespaces called `text`. TextBlob should now be imported with ``from textblob import TextBlob``.
- Update pattern resources for improved parser accuracy.
- Update NLTK.
- Allow Translator to connect to proxy server.
- PerceptronTagger completely deprecated. Install the ``textblob-aptagger`` extension instead.

0.7.1 (2013-09-30)
------------------
- Bugfix updates.
- Fix bug in feature extraction for ``NaiveBayesClassifier``.
- ``basic_extractor`` is now case-sensitive, e.g. contains(I) != contains(i)
- Fix ``repr`` output when a TextBlob contains non-ascii characters.
- Fix part-of-speech tagging with ``PatternTagger`` on Windows.
- Suppress warning about not having scikit-learn installed.

0.7.0 (2013-09-25)
------------------
- Wordnet integration. ``Word`` objects have ``synsets`` and ``definitions`` properties. The ``text.wordnet`` module allows you to create ``Synset`` and ``Lemma`` objects directly.
- Move all English-specific code to its own module, ``text.en``.
- Basic extensions framework in place. TextBlob has been refactored to make it easier to develop extensions.
- Add ``text.classifiers.PositiveNaiveBayesClassifier``.
- Update NLTK.
- ``NLTKTagger`` now working on Python 3.
- Fix ``__str__`` behavior. ``print(blob)`` should now print non-ascii text correctly in both Python 2 and 3.
- *Backwards-incompatible*: All abstract base classes have been moved to the ``text.base`` module.
- *Backwards-incompatible*: ``PerceptronTagger`` will now be maintained as an extension, ``textblob-aptagger``. Instantiating a ``text.taggers.PerceptronTagger()`` will raise a ``DeprecationWarning``.

0.6.3 (2013-09-15)
------------------
- Word tokenization fix: Words that stem from a contraction will still have an apostrophe, e.g. ``"Let's" => ["Let", "'s"]``.
- Fix bug with comparing blobs to strings.
- Add ``text.taggers.PerceptronTagger``, a fast and accurate POS tagger. Thanks `@syllog1sm <http://github.com/syllog1sm>`_.
- Note for Python 3 users: You may need to update your corpora, since NLTK master has reorganized its corpus system. Just run ``curl https://raw.github.com/sloria/TextBlob/master/download_corpora.py | python`` again.
- Add ``download_corpora_lite.py`` script for getting the minimum corpora requirements for TextBlob's basic features.

0.6.2 (2013-09-05)
------------------
- Fix bug that resulted in a ``UnicodeEncodeError`` when tagging text with non-ascii characters.
- Add ``DecisionTreeClassifier``.
- Add ``labels()`` and ``train()`` methods to classifiers.

0.6.1 (2013-09-01)
------------------
- Classifiers can be trained and tested on CSV, JSON, or TSV data.
- Add basic WordNet lemmatization via the ``Word.lemma`` property.
- ``WordList.pluralize()`` and ``WordList.singularize()`` methods return ``WordList`` objects.

0.6.0 (2013-08-25)
------------------
- Add Naive Bayes classification. New ``text.classifiers`` module, ``TextBlob.classify()``, and ``Sentence.classify()`` methods.
- Add parsing functionality via the ``TextBlob.parse()`` method. The ``text.parsers`` module currently has one implementation (``PatternParser``).
- Add spelling correction. This includes the ``TextBlob.correct()`` and ``Word.spellcheck()`` methods.
- Update NLTK.
- Backwards incompatible: ``clean_html`` has been deprecated, just as it has in NLTK. Use Beautiful Soup's ``soup.get_text()`` method for HTML-cleaning instead.
- Slight API change to language translation: if ``from_lang`` isn't specified, attempts to detect the language.
- Add ``itokenize()`` method to tokenizers that returns a generator instead of a list of tokens.

0.5.3 (2013-08-21)
------------------
- Unicode fixes: This fixes a bug that sometimes raised a ``UnicodeEncodeError`` upon creating accessing ``sentences`` for TextBlobs with non-ascii characters.
- Update NLTK

0.5.2 (2013-08-14)
------------------
- `Important patch update for NLTK users`: Fix bug with importing TextBlob if local NLTK is installed.
- Fix bug with computing start and end indices of sentences.


0.5.1 (2013-08-13)
------------------
- Fix bug that disallowed display of non-ascii characters in the Python REPL.
- Backwards incompatible: Restore ``blob.json`` property for backwards compatibility with textblob<=0.3.10. Add a ``to_json()`` method that takes the same arguments as ``json.dumps``.
- Add ``WordList.append`` and ``WordList.extend`` methods that append Word objects.

0.5.0 (2013-08-10)
------------------
- Language translation and detection API!
- Add ``text.sentiments`` module. Contains the ``PatternAnalyzer`` (default implementation) as well as a ``NaiveBayesAnalyzer``.
- Part-of-speech tags can be accessed via ``TextBlob.tags`` or ``TextBlob.pos_tags``.
- Add ``polarity`` and ``subjectivity`` helper properties.

0.4.0 (2013-08-05)
------------------
- New ``text.tokenizers`` module with ``WordTokenizer`` and ``SentenceTokenizer``. Tokenizer instances (from either textblob itself or NLTK) can be passed to TextBlob's constructor. Tokens are accessed through the new ``tokens`` property.
- New ``Blobber`` class for creating TextBlobs that share the same tagger, tokenizer, and np_extractor.
- Add ``ngrams`` method.
- `Backwards-incompatible`: ``TextBlob.json()`` is now a method, not a property. This allows you to pass arguments (the same that you would pass to ``json.dumps()``).
- New home for documentation: https://textblob.readthedocs.org/
- Add parameter for cleaning HTML markup from text.
- Minor improvement to word tokenization.
- Updated NLTK.
- Fix bug with adding blobs to bytestrings.

0.3.10 (2013-08-02)
-------------------
- Bundled NLTK no longer overrides local installation.
- Fix sentiment analysis of text with non-ascii characters.

0.3.9 (2013-07-31)
------------------
- Updated nltk.
- ConllExtractor is now Python 3-compatible.
- Improved sentiment analysis.
- Blobs are equal (with `==`) to their string counterparts.
- Added instructions to install textblob without nltk bundled.
- Dropping official 3.1 and 3.2 support.

0.3.8 (2013-07-30)
------------------
- Importing TextBlob is now **much faster**. This is because the noun phrase parsers are trained only on the first call to ``noun_phrases`` (instead of training them every time you import TextBlob).
- Add text.taggers module which allows user to change which POS tagger implementation to use. Currently supports PatternTagger and NLTKTagger (NLTKTagger only works with Python 2).
- NPExtractor and Tagger objects can be passed to TextBlob's constructor.
- Fix bug with POS-tagger not tagging one-letter words.
- Rename text/np_extractor.py -> text/np_extractors.py
- Add run_tests.py script.

0.3.7 (2013-07-28)
------------------

- Every word in a ``Blob`` or ``Sentence`` is a ``Word`` instance which has methods for inflection, e.g ``word.pluralize()`` and ``word.singularize()``.

- Updated the ``np_extractor`` module. Now has an new implementation, ``ConllExtractor`` that uses the Conll2000 chunking corpus. Only works on Py2.


%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
