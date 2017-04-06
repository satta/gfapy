from ..common.alignment_type import AlignmentType
from ..common.from_to import FromTo
from ..gfa1.to_gfa2 import ToGFA2 as GFA1_ToGFA2
from ..gfa1.references import References as GFA1_References
from ..gfa1.oriented_segments import OrientedSegments
from ..gfa1.alignment_type import AlignmentType as GFA1_AlignmentType
from ..gfa1.other import Other
from .canonical import Canonical
from .complement import Complement
from .equivalence import Equivalence
from .references import References as Link_References
from .to_gfa2 import ToGFA2 as Link_ToGFA2
from ..edge import Edge

class Link(Link_ToGFA2, GFA1_ToGFA2, Link_References, Equivalence, Complement, \
    Canonical, Other, GFA1_AlignmentType, OrientedSegments, GFA1_References, \
    AlignmentType, FromTo, Edge):
  """A link line (L) of a GFA1 file.

  Note:
    from_segment and to_segment are used instead of from/to
    as from is not a valid method name in Python. However, when not
    used as method name (e.g. as argument of get()), from and to can
    be used, as an alias has been defined.
  """

  RECORD_TYPE = "L"
  POSFIELDS = ["from_segment", "from_orient", "to_segment", "to_orient",
               "overlap"]
  PREDEFINED_TAGS = ["MQ", "NM", "RC", "FC", "KC"]
  FIELD_ALIAS = {"from": "from_segment", "to": "to_segment"}
  DATATYPE = {
    "from_segment" : "segment_name_gfa1",
    "from_orient" : "orientation",
    "to_segment" : "segment_name_gfa1",
    "to_orient" : "orientation",
    "overlap" : "alignment_gfa1",
    "MQ" : "i",
    "NM" : "i",
    "RC" : "i",
    "FC" : "i",
    "KC" : "i",
  }
  NAME_FIELD = "id"
  REFERENCE_FIELDS = ["from_segment", "to_segment"]
  BACKREFERENCE_RELATED_FIELDS = ["to_orient", "from_orient", "overlap"]
  DEPENDENT_LINES = ["paths"]

Link._apply_definitions()
