import gfapy

class Init:

  @property
  def positional_fieldnames(self):
    return self._positional_fieldnames

  @property
  def tagnames(self):
    return[x for x in self._data.keys() \
             if (not x in self.positional_fieldnames) \
                 and(not x in ["record_type"])]

  def _initialize_positional_fields(self, strings):
    """delayed, see #delayed_inizialize_positional_fields"""
    pass

  def _initialize_tags(self, strings):
    first_tag = len(strings)
    for i in range(len(strings)-1, 0, -1):
      try:
        self._initialize_tag(*(gfapy.field.parse_gfa_tag(strings[i])))
      except:
        break
      first_tag = i
    self._delayed_initialize_positional_fields(strings, first_tag)

  def _delayed_initialize_positional_fields(self, strings, n_positional_fields):
    self._positional_fieldnames = []
    self._init_field_value("record_type", "custom_record_type", strings[0],
                     errmsginfo = strings)
    for i in range(1, n_positional_fields):
      n = "field{}".format(i)
      self._init_field_value(n, "generic", strings[i], errmsginfo = strings)
      self.positional_fieldnames.append(n)
      self._datatype[n] = "generic"
