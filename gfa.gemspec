Gem::Specification.new do |s|
  s.name = 'gfa'
  s.version = '0.9'
  s.date = '2016-05-12'
  s.summary = 'Parse, edit and write GFA-format graphs in Ruby'
  s.description = <<-EOF
    The Graphical Fragment Assembly (GFA) is a proposed format which allow
    to describe the product of sequence assembly.
    This gem implements the proposed specifications for the GFA format
    described under https://github.com/pmelsted/GFA-spec/blob/master/GFA-spec.md
    as close as possible.
    The library allows to create a GFA object from a file in the GFA format
    or from scratch, to enumerate the graph elements (segments, links,
    containments, paths and header lines), to traverse the graph (by
    traversing all links outgoing from or incoming to a segment), to search for
    elements (e.g. which links connect two segments) and to manipulate the
    graph (e.g. to eliminate a link or a segment or to duplicate a segment
    distributing the read counts evenly on the copies).
  EOF
  s.author = 'Giorgio Gonnella'
  s.email = 'gonnella@zbh.uni-hamburg.de'
  s.files = ['lib/gfa.rb', 'lib/gfa/edit.rb', 'lib/gfa/line_getters.rb',
             'lib/gfa/line_setters.rb', 'lib/gfa/traverse.rb',
             'lib/gfa/connect.rb', 'lib/gfa/line.rb',
             'lib/gfa/cigar.rb', 'lib/gfa/sequence.rb',
             'lib/gfa/optfield.rb', 'lib/gfa/line/header.rb',
             'lib/gfa/line/containment.rb', 'lib/gfa/line/link.rb',
             'lib/gfa/line/segment.rb', 'lib/gfa/line/path.rb']
  s.homepage = 'http://github.com/ggonnella/ruby-gfa'
  s.license = 'CC-BY-SA'
  s.required_ruby_version = '>= 2.0'
end
