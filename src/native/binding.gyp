{
  'conditions': [
    [ 'OS=="win"', {
      'variables': {}
    }, { # 'OS!="win"'
      'variables': {}
    }]
  ],
  'targets': [
    {
      'target_name': 'hello',
      "sources": [ 
        "src/webcam_api.cpp",
        "src/video.cpp",
        "src/video_source.cpp"
      ],
      'include_dirs': [
        "<!@(node -p \"require('node-addon-api').include\")",
        'src/',
        '/usr/local/lib/',
      ],
      'link_settings': {
        'libraries': [
          '/usr/local/lib/libavcodec.59.18.100.dylib',
          '/usr/local/lib/libavdevice.59.4.100.dylib',
          '/usr/local/lib/libavfilter.8.24.100.dylib',
          '/usr/local/lib/libavformat.59.16.100.dylib',
          '/usr/local/lib/libavutil.57.17.100.dylib',
          '/usr/local/lib/libpostproc.56.3.100.dylib',
          '/usr/local/lib/libswresample.4.3.100.dylib',
          '/usr/local/lib/libswscale.6.4.100.dylib',
        ],
        'library_dirs': [
          '/usr/local/lib/'
        ]
      },
      'conditions': [
        [ 'OS=="win"', {
          'sources': [],
          'msvs_settings': {
            'VCCLCompilerTool': {
              'ExceptionHandling': 1, # /EHsc
              'WarnAsError': 'true'
            }
          },
          'msvs_disabled_warnings': [
            4018,  # signed/unsigned mismatch
            4244,  # conversion from 'type1' to 'type2', possible loss of data
            4267,  # conversion from 'size_t' to 'type', possible loss of data
            4530,  # C++ exception handler used, but unwind semantics are not enabled
            4506,  # no definition for inline function
            4996,  # function was declared deprecated
          ],
          'defines': [
            '_WIN32_WINNT=0x0600'
          ]
        }], # OS=="win"
        [ 'OS=="mac"', {
          'sources': [],
          'xcode_settings': {
            'OTHER_CPLUSPLUSFLAGS' : [
              '-std=c++11',
              '-stdlib=libc++',
              '-D__STDC_CONSTANT_MACROS'
            ],
            'OTHER_LDFLAGS': [
              '-stdlib=libc++',
              '-framework CoreFoundation',
              '-framework VideoDecodeAcceleration',
              '-framework QuartzCore',
              '-Wl,-framework,Cocoa'
            ],
            'MACOSX_DEPLOYMENT_TARGET': '10.7'
          }
        }], # OS=="mac"
        [ 'OS=="linux"', {
          'sources': []
        }]
      ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ]
    }
  ]
}
