test_text = """<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF xml:base="http://www.gutenberg.org/"
  xmlns:cc="http://web.resource.org/cc/"
  xmlns:dcam="http://purl.org/dc/dcam/"
  xmlns:pgterms="http://www.gutenberg.org/2009/pgterms/"
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:marcrel="http://id.loc.gov/vocabulary/relators/"
  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
>
  <pgterms:ebook rdf:about="ebooks/46">
    <dcterms:hasFormat>
      <pgterms:file rdf:about="http://www.gutenberg.org/ebooks/46.rdf">
        <dcterms:isFormatOf rdf:resource="ebooks/46"/>
        <dcterms:extent rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">17665</dcterms:extent>
        <dcterms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2017-10-19T05:01:10.252670</dcterms:modified>
        <dcterms:format>
          <rdf:Description rdf:nodeID="N137277c1e48e48e39ef4ce00180c877b">
            <rdf:value rdf:datatype="http://purl.org/dc/terms/IMT">application/rdf+xml</rdf:value>
            <dcam:memberOf rdf:resource="http://purl.org/dc/terms/IMT"/>
          </rdf:Description>
        </dcterms:format>
      </pgterms:file>
    </dcterms:hasFormat>
    <dcterms:hasFormat>
      <pgterms:file rdf:about="http://www.gutenberg.org/files/46/46-8.zip">
        <dcterms:extent rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">71158</dcterms:extent>
        <dcterms:isFormatOf rdf:resource="ebooks/46"/>
        <dcterms:format>
          <rdf:Description rdf:nodeID="N61c659bf3bd44f8c9b8fb935d5c41dd1">
            <dcam:memberOf rdf:resource="http://purl.org/dc/terms/IMT"/>
            <rdf:value rdf:datatype="http://purl.org/dc/terms/IMT">text/plain; charset=iso-8859-1</rdf:value>
          </rdf:Description>
        </dcterms:format>
        <dcterms:format>
          <rdf:Description rdf:nodeID="Nb879197261354b9c89c285136ce9b588">
            <dcam:memberOf rdf:resource="http://purl.org/dc/terms/IMT"/>
            <rdf:value rdf:datatype="http://purl.org/dc/terms/IMT">application/zip</rdf:value>
          </rdf:Description>
        </dcterms:format>
        <dcterms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2004-08-11T12:27:34</dcterms:modified>
      </pgterms:file>
    </dcterms:hasFormat>
    <pgterms:downloads rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">4764</pgterms:downloads>
    <dcterms:hasFormat>
      <pgterms:file rdf:about="http://www.gutenberg.org/cache/epub/46/pg46.cover.small.jpg">
        <dcterms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2017-10-01T01:08:39.912741</dcterms:modified>
        <dcterms:extent rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">2180</dcterms:extent>
        <dcterms:format>
          <rdf:Description rdf:nodeID="N1b833b23768d4a6fb91c70d4324a2b27">
            <rdf:value rdf:datatype="http://purl.org/dc/terms/IMT">image/jpeg</rdf:value>
            <dcam:memberOf rdf:resource="http://purl.org/dc/terms/IMT"/>
          </rdf:Description>
        </dcterms:format>
        <dcterms:isFormatOf rdf:resource="ebooks/46"/>
      </pgterms:file>
    </dcterms:hasFormat>
    <pgterms:marc901>file:///public/vhost/g/gutenberg/html/files/46/46-h/images/bookcover.jpg</pgterms:marc901>
    <dcterms:subject>
      <rdf:Description rdf:nodeID="N928c9d0bb5a84b35966c3dae6fa6c643">
        <dcam:memberOf rdf:resource="http://purl.org/dc/terms/LCSH"/>
        <rdf:value>Misers -- Fiction</rdf:value>
      </rdf:Description>
    </dcterms:subject>
    <dcterms:hasFormat>
      <pgterms:file rdf:about="http://www.gutenberg.org/ebooks/46.epub.images">
        <dcterms:format>
          <rdf:Description rdf:nodeID="Nb1b66c7b382a4c3c9bb659a47d1690a8">
            <rdf:value rdf:datatype="http://purl.org/dc/terms/IMT">application/epub+zip</rdf:value>
            <dcam:memberOf rdf:resource="http://purl.org/dc/terms/IMT"/>
          </rdf:Description>
        </dcterms:format>
        <dcterms:isFormatOf rdf:resource="ebooks/46"/>
        <dcterms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2017-10-01T01:08:36.873837</dcterms:modified>
        <dcterms:extent rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">548045</dcterms:extent>
      </pgterms:file>
    </dcterms:hasFormat>
    <dcterms:hasFormat>
      <pgterms:file rdf:about="http://www.gutenberg.org/files/46/46.zip">
        <dcterms:format>
          <rdf:Description rdf:nodeID="Ne9f3fc9b35b949569337e2e43204e76b">
            <rdf:value rdf:datatype="http://purl.org/dc/terms/IMT">text/plain; charset=us-ascii</rdf:value>
            <dcam:memberOf rdf:resource="http://purl.org/dc/terms/IMT"/>
          </rdf:Description>
        </dcterms:format>
        <dcterms:format>
          <rdf:Description rdf:nodeID="Nb10af6e2071c46a9ab6939380e7847bf">
            <rdf:value rdf:datatype="http://purl.org/dc/terms/IMT">application/zip</rdf:value>
            <dcam:memberOf rdf:resource="http://purl.org/dc/terms/IMT"/>
          </rdf:Description>
        </dcterms:format>
        <dcterms:isFormatOf rdf:resource="ebooks/46"/>
        <dcterms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2004-08-11T12:27:34</dcterms:modified>
        <dcterms:extent rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">71138</dcterms:extent>
      </pgterms:file>
    </dcterms:hasFormat>
    <dcterms:hasFormat>
      <pgterms:file rdf:about="http://www.gutenberg.org/cache/epub/46/pg46.cover.medium.jpg">
        <dcterms:extent rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">14887</dcterms:extent>
        <dcterms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2017-10-01T01:08:39.960746</dcterms:modified>
        <dcterms:isFormatOf rdf:resource="ebooks/46"/>
        <dcterms:format>
          <rdf:Description rdf:nodeID="N9b258d5d8be742b981ae0c0b2fb5d3f5">
            <dcam:memberOf rdf:resource="http://purl.org/dc/terms/IMT"/>
            <rdf:value rdf:datatype="http://purl.org/dc/terms/IMT">image/jpeg</rdf:value>
          </rdf:Description>
        </dcterms:format>
      </pgterms:file>
    </dcterms:hasFormat>
    <dcterms:hasFormat>
      <pgterms:file rdf:about="http://www.gutenberg.org/files/46/46.txt">
        <dcterms:isFormatOf rdf:resource="ebooks/46"/>
        <dcterms:extent rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">182021</dcterms:extent>
        <dcterms:format>
          <rdf:Description rdf:nodeID="Nb20c6827705f4ba08feb01abe8ccec3c">
            <dcam:memberOf rdf:resource="http://purl.org/dc/terms/IMT"/>
            <rdf:value rdf:datatype="http://purl.org/dc/terms/IMT">text/plain; charset=us-ascii</rdf:value>
          </rdf:Description>
        </dcterms:format>
        <dcterms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2004-08-11T12:16:42</dcterms:modified>
      </pgterms:file>
    </dcterms:hasFormat>
    <dcterms:creator>
      <pgterms:agent rdf:about="2009/agents/37">
        <pgterms:name>Dickens, Charles</pgterms:name>
        <pgterms:alias>Dickens, Charles John Huffam</pgterms:alias>
        <pgterms:deathdate rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1870</pgterms:deathdate>
        <pgterms:webpage rdf:resource="http://en.wikipedia.org/wiki/Charles_Dickens"/>
        <pgterms:alias>Boz</pgterms:alias>
        <pgterms:birthdate rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1812</pgterms:birthdate>
      </pgterms:agent>
    </dcterms:creator>
    <dcterms:subject>
      <rdf:Description rdf:nodeID="N54505243599f4a1f80a72f4f14e72fcc">
        <rdf:value>Christmas stories</rdf:value>
        <dcam:memberOf rdf:resource="http://purl.org/dc/terms/LCSH"/>
      </rdf:Description>
    </dcterms:subject>
    <pgterms:bookshelf>
      <rdf:Description rdf:nodeID="Nc3227854252d429792348969505bafd9">
        <rdf:value>Christmas</rdf:value>
        <dcam:memberOf rdf:resource="2009/pgterms/Bookshelf"/>
      </rdf:Description>
    </pgterms:bookshelf>
    <dcterms:hasFormat>
      <pgterms:file rdf:about="http://www.gutenberg.org/ebooks/46.txt.utf-8">
        <dcterms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2017-10-01T01:08:36.241830</dcterms:modified>
        <dcterms:isFormatOf rdf:resource="ebooks/46"/>
        <dcterms:extent rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">181997</dcterms:extent>
        <dcterms:format>
          <rdf:Description rdf:nodeID="N06d5177ae1c440faac503d2b1c92882f">
            <rdf:value rdf:datatype="http://purl.org/dc/terms/IMT">text/plain</rdf:value>
            <dcam:memberOf rdf:resource="http://purl.org/dc/terms/IMT"/>
          </rdf:Description>
        </dcterms:format>
      </pgterms:file>
    </dcterms:hasFormat>
    <dcterms:rights>Public domain in the USA.</dcterms:rights>
    <dcterms:type>
      <rdf:Description rdf:nodeID="Na48f3a855c9d48c2ab5abd999f28d580">
        <dcam:memberOf rdf:resource="http://purl.org/dc/terms/DCMIType"/>
        <rdf:value>Text</rdf:value>
      </rdf:Description>
    </dcterms:type>
    <dcterms:subject>
      <rdf:Description rdf:nodeID="N84e73afafb794d5590b60a5ddc1e28f6">
        <rdf:value>Scrooge, Ebenezer (Fictitious character) -- Fiction</rdf:value>
        <dcam:memberOf rdf:resource="http://purl.org/dc/terms/LCSH"/>
      </rdf:Description>
    </dcterms:subject>
    <marcrel:ill>
      <pgterms:agent rdf:about="2009/agents/9473">
        <pgterms:alias>Leech, J. (John)</pgterms:alias>
        <pgterms:deathdate rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1864</pgterms:deathdate>
        <pgterms:webpage rdf:resource="http://en.wikipedia.org/wiki/John_Leech_%28caricaturist%29"/>
        <pgterms:name>Leech, John</pgterms:name>
        <pgterms:birthdate rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1817</pgterms:birthdate>
      </pgterms:agent>
    </marcrel:ill>
    <dcterms:hasFormat>
      <pgterms:file rdf:about="http://www.gutenberg.org/ebooks/46.epub.noimages">
        <dcterms:extent rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">136532</dcterms:extent>
        <dcterms:format>
          <rdf:Description rdf:nodeID="N2dc39f65e7744472ab28e3d09c4a3d43">
            <rdf:value rdf:datatype="http://purl.org/dc/terms/IMT">application/epub+zip</rdf:value>
            <dcam:memberOf rdf:resource="http://purl.org/dc/terms/IMT"/>
          </rdf:Description>
        </dcterms:format>
        <dcterms:isFormatOf rdf:resource="ebooks/46"/>
        <dcterms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2017-10-01T01:08:37.205821</dcterms:modified>
      </pgterms:file>
    </dcterms:hasFormat>
    <dcterms:subject>
      <rdf:Description rdf:nodeID="Nc8e73a0c1bb441cd994e78f122deb9a3">
        <dcam:memberOf rdf:resource="http://purl.org/dc/terms/LCSH"/>
        <rdf:value>Ghost stories</rdf:value>
      </rdf:Description>
    </dcterms:subject>
    <dcterms:publisher>Project Gutenberg</dcterms:publisher>
    <dcterms:hasFormat>
      <pgterms:file rdf:about="http://www.gutenberg.org/files/46/46-h.zip">
        <dcterms:isFormatOf rdf:resource="ebooks/46"/>
        <dcterms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2013-12-20T08:40:26</dcterms:modified>
        <dcterms:format>
          <rdf:Description rdf:nodeID="N01df38f2908740649dd9d1d2d19547f7">
            <rdf:value rdf:datatype="http://purl.org/dc/terms/IMT">text/html; charset=iso-8859-1</rdf:value>
            <dcam:memberOf rdf:resource="http://purl.org/dc/terms/IMT"/>
          </rdf:Description>
        </dcterms:format>
        <dcterms:extent rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">542792</dcterms:extent>
        <dcterms:format>
          <rdf:Description rdf:nodeID="N1af28a6914f946a2b7c147992455ee8e">
            <dcam:memberOf rdf:resource="http://purl.org/dc/terms/IMT"/>
            <rdf:value rdf:datatype="http://purl.org/dc/terms/IMT">application/zip</rdf:value>
          </rdf:Description>
        </dcterms:format>
      </pgterms:file>
    </dcterms:hasFormat>
    <dcterms:title>A Christmas Carol in Prose; Being a Ghost Story of Christmas</dcterms:title>
    <dcterms:issued rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2004-08-11</dcterms:issued>
    <dcterms:hasFormat>
      <pgterms:file rdf:about="http://www.gutenberg.org/files/46/46-8.txt">
        <dcterms:extent rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">182029</dcterms:extent>
        <dcterms:format>
          <rdf:Description rdf:nodeID="N56539be98d1b42879d9021e0ba0214d2">
            <rdf:value rdf:datatype="http://purl.org/dc/terms/IMT">text/plain; charset=iso-8859-1</rdf:value>
            <dcam:memberOf rdf:resource="http://purl.org/dc/terms/IMT"/>
          </rdf:Description>
        </dcterms:format>
        <dcterms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2004-08-11T12:16:42</dcterms:modified>
        <dcterms:isFormatOf rdf:resource="ebooks/46"/>
      </pgterms:file>
    </dcterms:hasFormat>
    <dcterms:subject>
      <rdf:Description rdf:nodeID="N7e0bc7e9e5244a5a9f5b967824012318">
        <dcam:memberOf rdf:resource="http://purl.org/dc/terms/LCSH"/>
        <rdf:value>London (England) -- Fiction</rdf:value>
      </rdf:Description>
    </dcterms:subject>
    <pgterms:bookshelf>
      <rdf:Description rdf:nodeID="Nd009ae414944401cbfa41aa894bb3127">
        <dcam:memberOf rdf:resource="2009/pgterms/Bookshelf"/>
        <rdf:value>Children's Literature</rdf:value>
      </rdf:Description>
    </pgterms:bookshelf>
    <dcterms:subject>
      <rdf:Description rdf:nodeID="N9ee8f1cbbb1c4c7995ac9a2086549126">
        <rdf:value>Sick children -- Fiction</rdf:value>
        <dcam:memberOf rdf:resource="http://purl.org/dc/terms/LCSH"/>
      </rdf:Description>
    </dcterms:subject>
    <dcterms:subject>
      <rdf:Description rdf:nodeID="N834593b0349945b69d3e94bc630123b1">
        <dcam:memberOf rdf:resource="http://purl.org/dc/terms/LCC"/>
        <rdf:value>PR</rdf:value>
      </rdf:Description>
    </dcterms:subject>
    <dcterms:hasFormat>
      <pgterms:file rdf:about="http://www.gutenberg.org/files/46/46-h/46-h.htm">
        <dcterms:isFormatOf rdf:resource="ebooks/46"/>
        <dcterms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2013-12-20T08:37:42</dcterms:modified>
        <dcterms:format>
          <rdf:Description rdf:nodeID="N1e17d47b7ef146cb9ec8a3ea9238109d">
            <dcam:memberOf rdf:resource="http://purl.org/dc/terms/IMT"/>
            <rdf:value rdf:datatype="http://purl.org/dc/terms/IMT">text/html; charset=iso-8859-1</rdf:value>
          </rdf:Description>
        </dcterms:format>
        <dcterms:extent rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">235120</dcterms:extent>
      </pgterms:file>
    </dcterms:hasFormat>
    <dcterms:license rdf:resource="license"/>
    <dcterms:subject>
      <rdf:Description rdf:nodeID="Nff560e5ce31f40b489dcd6bab19767de">
        <dcam:memberOf rdf:resource="http://purl.org/dc/terms/LCSH"/>
        <rdf:value>Poor families -- Fiction</rdf:value>
      </rdf:Description>
    </dcterms:subject>
    <dcterms:hasFormat>
      <pgterms:file rdf:about="http://www.gutenberg.org/ebooks/46.kindle.noimages">
        <dcterms:isFormatOf rdf:resource="ebooks/46"/>
        <dcterms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2017-10-01T01:08:39.861748</dcterms:modified>
        <dcterms:format>
          <rdf:Description rdf:nodeID="N5aadf8b9cda545ada5d9e250b64c70ce">
            <dcam:memberOf rdf:resource="http://purl.org/dc/terms/IMT"/>
            <rdf:value rdf:datatype="http://purl.org/dc/terms/IMT">application/x-mobipocket-ebook</rdf:value>
          </rdf:Description>
        </dcterms:format>
        <dcterms:extent rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">458828</dcterms:extent>
      </pgterms:file>
    </dcterms:hasFormat>
    <dcterms:language>
      <rdf:Description rdf:nodeID="Nc6ec8cff39bc4daa8f95749889511e40">
        <rdf:value rdf:datatype="http://purl.org/dc/terms/RFC4646">en</rdf:value>
      </rdf:Description>
    </dcterms:language>
    <dcterms:hasFormat>
      <pgterms:file rdf:about="http://www.gutenberg.org/ebooks/46.kindle.images">
        <dcterms:format>
          <rdf:Description rdf:nodeID="N04d55f3ffb84458d9b6da3bea57b0947">
            <dcam:memberOf rdf:resource="http://purl.org/dc/terms/IMT"/>
            <rdf:value rdf:datatype="http://purl.org/dc/terms/IMT">application/x-mobipocket-ebook</rdf:value>
          </rdf:Description>
        </dcterms:format>
        <dcterms:extent rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1281185</dcterms:extent>
        <dcterms:modified rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">2017-10-01T01:08:38.714778</dcterms:modified>
        <dcterms:isFormatOf rdf:resource="ebooks/46"/>
      </pgterms:file>
    </dcterms:hasFormat>
  </pgterms:ebook>
  <cc:Work rdf:about="">
    <cc:license rdf:resource="https://creativecommons.org/publicdomain/zero/1.0/"/>
    <rdfs:comment>Archives containing the RDF files for *all* our books can be downloaded at
            http://www.gutenberg.org/wiki/Gutenberg:Feeds#The_Complete_Project_Gutenberg_Catalog</rdfs:comment>
  </cc:Work>
  <rdf:Description rdf:about="http://en.wikipedia.org/wiki/Charles_Dickens">
    <dcterms:description>Wikipedia</dcterms:description>
  </rdf:Description>
  <rdf:Description rdf:about="http://en.wikipedia.org/wiki/John_Leech_%28caricaturist%29">
    <dcterms:description>en.wikipedia</dcterms:description>
  </rdf:Description>
</rdf:RDF>
"""


def get_author(text):
    """
    :param text: the text of an rdf file
    :return: the author of the ressource
    (which is contained in the <pgterms:name>Dickens, Charles</pgterms:name> line)
    """
    name = ""
    balise_1 = "<dcterms:creator>"
    balise_2 = "<pgterms:name>"
    for i in range(len(text)):
        if text[i:i+len(balise_1)] in balise_1:
            j = i + len(balise_1)
            while text[j:j+len(balise_2)] not in balise_2:
                j += 1
            l = j + len(balise_2)
            while text[l] != "<":
                name += text[l]
                l += 1
            break

    return name


def get_language(text):
    """
    <dcterms:language>
      <rdf:Description rdf:nodeID="N8b71b206837842439a9e2602140d6f82">
        <rdf:value rdf:datatype="http://purl.org/dc/terms/RFC4646">fr</rdf:value>
      </rdf:Description>
    </dcterms:language>
    """
    name = ""
    balise_1 = "<dcterms:language>"
    balise_2 = """<rdf:value rdf:datatype="http://purl.org/dc/terms/RFC4646">"""
    for i in range(len(text)):
        if text[i:i+len(balise_1)] in balise_1:
            j = i + len(balise_1)
            while text[j:j+len(balise_2)] not in balise_2:
                j += 1
            l = j + len(balise_2)
            while text[l] != "<":
                name += text[l]
                l += 1
            break

    return name


def get_title(text):
    """
    :param text: the text of an rdf file
    :return: the author of the ressource
    (which is contained in the <pgterms:name>Dickens, Charles</pgterms:name> line)
    """
    name = ""
    balise_1 = "<dcterms:title>"
    for i in range(len(text)):
        if text[i:i+len(balise_1)] in balise_1:
            j = i + len(balise_1)
            while text[j] != "<":
                name += text[j]
                j += 1
            break
    return name












