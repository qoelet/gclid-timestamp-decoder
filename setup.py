from setuptools import setup

setup(name='gclid-timestamp-decoder',
      version='0.1.2',
      description='Decoding timestamp from Google gclid using Protocol Buffers.',
      author='Kenny Shen',
      author_email='kenny@machinesung.com',
      license='BSD',
      url='https://github.com/qoelet/gclid-timestamp-decoder',
      download_url='https://pypi.python.org/pypi/gclid-timestamp-decoder',
      install_requires=['protobuf==2.6'],
      packages=['gclid_timestamp_decoder']
    )
