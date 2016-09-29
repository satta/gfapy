import gfapy

class Connection:

  def is_connected(self):
    """
    In a connected line, some of the fields are converted
    into references or a list of references to other lines.
    Furthermore instance variables are populated with back
    references to the line (e.g. connection of a segment
    are stored as references in segment arrays), to allow
    graph traversal.

    Returns
    -------
    bool
      Is the line connected to other lines of a GFA instance?
    """
    return (self.gfa is not None)

  @property
  def gfa(self):
    return self._gfa

  def connect(self, gfa):
    """
    Connect the line to a GFA instance

    Parameters
    ----------
    gfa : GFA
      the GFA instance

    Returns
    -------
    None
    """
    if self.connected():
      raise gfapy.RuntimeError(
        "Line {} is already connected to a GFA instance".format(self))
    previous = gfa.search_duplicate(self)
    if previous:
      if previous.virtual():
        return self._substitute_virtual_line(previous)
      else:
        return self._process_not_unique(previous)
    else:
      self.gfa = gfa
      self._initialize_references()
      self.gfa.register_line(self)
      return None

  def add_reference(self, line, key, append = True):
    if not self.refs: self.refs = {}
    if not self.refs[key]: self.refs[key] = []
    if append:
      self.refs[key].append(line)
    else:
      self.refs[key].insert(0, line)

  def _refs(self):
    if not self.refs: self.refs = {}

  def _initialize_references(self):
    """
    .. note::
      SUBCLASSES with reference fields shall
      overwrite this method to connect their reference
      fields
    """
    pass

  def _process_not_unique(self, previous):
    """
    .. note::
      SUBCLASSES may overwrite this method
      if some kind of non unique lines shall be
      tolerated or handled differently (eg complement links)
    """
    raise gfapy.NotUniqueError(
      "Line: {}\n".format(str(self))+
      "Line or ID not unique\n"+
      "Matching previous line: {}".format(str(previous))
      )
