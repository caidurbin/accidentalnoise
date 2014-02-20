Pod::Spec.new do |s|
  s.name         = "accidentalnoise"
  s.version      = "1.0.0"
  s.summary      = "Accidental Noise Library is a library for generating Perlin noise and other forms of noise in a modular fashion."
  s.description  = "Accidental Noise Library is a library for generating Perlin noise and other forms of noise in a modular fashion. Functions provide 2D, 3D, 4D and 6D variants, and provide an interface for chaining functions together to build up complex functions out of simple pieces. ANL provides function sets that output either double-precision floating point values (for working with the noise signals directly) or RGBA values (for compositing noise functions into RGBA colors.) Various modules are provided to generate, modify, combine, and transform functions to produce a complex output."
  s.homepage     = "https://github.com/caidurbin/accidentalnoise"
  s.license      = 'LICENSE'
  s.author       = "Joshua Tippetts"
  s.source       = { :git => 'https://github.com/caidurbin/accidentalnoise.git', :tag => s.version.to_s }
  
  s.source_files = 'include/**/*.h', 'src/*.{h,cpp}'
  s.library      = 'c++'
  s.requires_arc = false

  s.ios.deployment_target = '5.0'
  s.osx.deployment_target = '10.7'


end