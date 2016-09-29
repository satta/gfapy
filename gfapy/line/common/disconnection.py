import gfapy

class Disconnection:

  def disconnect():
    """
    Remove the line from the GFA instance it belongs to, if any.

    The Line instance itself will still exist, but all references from it to
    other lines are deleted, as well as references to it from other lines.
    Mandatory references are turned into their non-reference representations
    (e.g. segments references in the sid fields of E lines
    or in the from/to lines of L/C lines are changed into symbols).
    """
    if not self.connected():
      raise gfapy.RuntimeError(
        "Line {} is not connected to a GFA instance".format(self))
    self._remove_field_backreferences()
    self._remove_field_references()
    self._disconnect_dependent_lines()
    self._remove_nonfield_backreferences()
    self._remove_nonfield_references()
    self.gfa.unregister_line(self)
    self.gfa = None

  def delete_reference(self, line, key):
    if not self.refs or not self.refs[key]:
      return
    idx = next((i for i,x in enumerate(self.refs[key]) if x == line), None)
    if not idx: return
    self.refs = (([] if idx == 0 else self.refs[0:idx-1]) + self.refs[idx+1:-1])

  def delete_first_reference(self, key):
    if not self.refs or not self.refs[key]:
      return
    self.refs[key].pop(0)

  def delete_last_reference(self, key):
    if not self.refs or not self.refs[key]:
      return
    self.refs[key].pop()

  def _remove_field_references(self):
    """
    .. note::
      currently this method supports fields which are: references,
      oriented lines and lists of references of oriented lines;
      if SUBCLASSES have reference fields which contain references
      in a different fashion, the method must be updated or overwritten
      in the subclass
    """
    for k in self.__class__.REFERENCE_FIELDS:
      ref = self.get(k)
      if isinstance(ref, gfapy.Line):
        self._set_existing_field(k, str(ref), set_reference = True)
      elif isinstance(ref, gfapy.OrientedLine):
        ref.line = ref.name
      elif isinstance(ref, list):
        for i, elem in enumerate(ref):
          if isinstance(elem, gfapy.Line):
            ref[i] = str(elem)
          elif isinstance(elem, gfapy.OrientedLine):
            ref[i].line = elem.name

  #def each_reference_in(field, &block)
  #  case field
  #  when RGFA::Line
  #    yield field
  #  when RGFA::OrientedLine
  #    yield field.line
  #  when Array
  #    field.each {|elem| each_reference_in(elem, &block)}
  #  end
  #end

  def _remove_backreference(self, ref, k):
    if isinstance(ref, gfapy.Line):
      ref.update_references(self, nil, k)
    elif isinstance(ref, gfapy.OrientedLine):
      ref.line.update_references(self, nil, k)
    elif isinstance(ref, list):
      for i in range(len(ref)):
       self._remove_backreference(ref[i], k)

  def _disconnect_dependent_line(self, ref):
    if isinstance(ref, gfapy.Line):
      ref.disconnect()
    elif isinstance(ref, gfapy.OrientedLine):
      ref.line.disconnect()
    elif isinstance(ref, list):
      for i in range(len(ref)):
        self._disconnect_dependent_line(ref[i])

  def _remove_field_backreferences(self):
    """
    .. note::
      currently this method supports fields which are: references,
      oriented lines and lists of references of oriented lines;
      if SUBCLASSES have reference fields which contain references
      in a different fashion, the method must be updated or overwritten
      in the subclass
    """
    for k in self.__class__.REFERENCE_FIELDS:
      self._remove_backreference(self.get(k), k)

  def _disconnect_dependent_lines(self):
    for k in self.__class__.DEPENDENT_LINES:
      for ref in refs.get(k, []):
        self._disconnect_dependent_line(ref)

  def _remove_nonfield_backreferences(self):
    for k in self.__class__.OTHER_REFERENCES:
      for ref in refs.get(k, []):
        self._remove_backreference(ref, k)

  def _remove_nonfield_references(self):
    self.refs = {}
