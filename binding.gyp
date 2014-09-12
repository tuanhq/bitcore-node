{
  'targets': [{
    'target_name': 'bitcoindjs',
    'include_dirs' : [
      '/usr/include',
      '<!(node -e "require(\'nan\')")',
      # './deps',
      '/usr/include/boost',
      '<!(echo "$HOME")/bitcoin/src/leveldb/include',
      '<!(echo "$HOME")/bitcoin/src',
    ],
    'sources': [
      './src/bitcoindjs.cc',
    ],
    'defines': [
      'HAVE_WORKING_BOOST_SLEEP',
      #'HAVE_WORKING_BOOST_SLEEP_FOR',
      'ENABLE_WALLET',
    ],
    'cflags_cc': [
      '-fexceptions',
      '-frtti',
    ],
    'libraries': [
      # standard libs:
      '-L/usr/lib',
      '-L/usr/local/lib',
      # boost:
      '-lboost_system',
      '-lboost_filesystem',
      '-lboost_program_options',
      '-lboost_thread',
      '-lboost_chrono',
      # leveldb:
      #'<!(echo "$HOME")/bitcoin/src/leveldb/libleveldb.a',
      # bitcoind:
      '<!(echo "$HOME")/bitcoin/src/libbitcoind.so',
    ]
  }]
}
