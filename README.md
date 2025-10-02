Last login: Wed Oct  1 19:45:59 on ttys000
medvr05@medvr05s-MacBook-Pro ~ % cd desktop
medvr05@medvr05s-MacBook-Pro desktop % cd xray-project
medvr05@medvr05s-MacBook-Pro xray-project % source venv/bin/activate
(venv) medvr05@medvr05s-MacBook-Pro xray-project % pip list | grep tensorflow
zsh: command not found: pip
(venv) medvr05@medvr05s-MacBook-Pro xray-project % pip install tensorflow numpy matplotlib pillow
zsh: command not found: pip
(venv) medvr05@medvr05s-MacBook-Pro xray-project % pip3 install tensorflow numpy matplotlib pillow
Collecting tensorflow
  Downloading tensorflow-2.20.0-cp313-cp313-macosx_12_0_arm64.whl.metadata (4.5 kB)
Collecting numpy
  Downloading numpy-2.3.3-cp313-cp313-macosx_14_0_arm64.whl.metadata (62 kB)
Collecting matplotlib
  Downloading matplotlib-3.10.6-cp313-cp313-macosx_11_0_arm64.whl.metadata (11 kB)
Collecting pillow
  Downloading pillow-11.3.0-cp313-cp313-macosx_11_0_arm64.whl.metadata (9.0 kB)
Collecting absl-py>=1.0.0 (from tensorflow)
  Using cached absl_py-2.3.1-py3-none-any.whl.metadata (3.3 kB)
Collecting astunparse>=1.6.0 (from tensorflow)
  Using cached astunparse-1.6.3-py2.py3-none-any.whl.metadata (4.4 kB)
Collecting flatbuffers>=24.3.25 (from tensorflow)
  Using cached flatbuffers-25.9.23-py2.py3-none-any.whl.metadata (875 bytes)
Collecting gast!=0.5.0,!=0.5.1,!=0.5.2,>=0.2.1 (from tensorflow)
  Using cached gast-0.6.0-py3-none-any.whl.metadata (1.3 kB)
Collecting google_pasta>=0.1.1 (from tensorflow)
  Using cached google_pasta-0.2.0-py3-none-any.whl.metadata (814 bytes)
Collecting libclang>=13.0.0 (from tensorflow)
  Using cached libclang-18.1.1-1-py2.py3-none-macosx_11_0_arm64.whl.metadata (5.2 kB)
Collecting opt_einsum>=2.3.2 (from tensorflow)
  Using cached opt_einsum-3.4.0-py3-none-any.whl.metadata (6.3 kB)
Collecting packaging (from tensorflow)
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Requirement already satisfied: protobuf>=5.28.0 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from tensorflow) (6.32.1)
Requirement already satisfied: requests<3,>=2.21.0 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from tensorflow) (2.32.5)
Requirement already satisfied: setuptools in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from tensorflow) (80.9.0)
Requirement already satisfied: six>=1.12.0 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from tensorflow) (1.17.0)
Collecting termcolor>=1.1.0 (from tensorflow)
  Using cached termcolor-3.1.0-py3-none-any.whl.metadata (6.4 kB)
Collecting typing_extensions>=3.6.6 (from tensorflow)
  Using cached typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting wrapt>=1.11.0 (from tensorflow)
  Downloading wrapt-1.17.3-cp313-cp313-macosx_11_0_arm64.whl.metadata (6.4 kB)
Collecting grpcio<2.0,>=1.24.3 (from tensorflow)
  Downloading grpcio-1.75.1-cp313-cp313-macosx_11_0_universal2.whl.metadata (3.7 kB)
Collecting tensorboard~=2.20.0 (from tensorflow)
  Using cached tensorboard-2.20.0-py3-none-any.whl.metadata (1.8 kB)
Collecting keras>=3.10.0 (from tensorflow)
  Downloading keras-3.11.3-py3-none-any.whl.metadata (5.9 kB)
Collecting h5py>=3.11.0 (from tensorflow)
  Downloading h5py-3.14.0-cp313-cp313-macosx_11_0_arm64.whl.metadata (2.7 kB)
Collecting ml_dtypes<1.0.0,>=0.5.1 (from tensorflow)
  Downloading ml_dtypes-0.5.3-cp313-cp313-macosx_10_13_universal2.whl.metadata (8.9 kB)
Requirement already satisfied: charset_normalizer<4,>=2 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from requests<3,>=2.21.0->tensorflow) (3.4.3)
Requirement already satisfied: idna<4,>=2.5 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from requests<3,>=2.21.0->tensorflow) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from requests<3,>=2.21.0->tensorflow) (2.5.0)
Requirement already satisfied: certifi>=2017.4.17 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from requests<3,>=2.21.0->tensorflow) (2025.8.3)
Collecting markdown>=2.6.8 (from tensorboard~=2.20.0->tensorflow)
  Using cached markdown-3.9-py3-none-any.whl.metadata (5.1 kB)
Collecting tensorboard-data-server<0.8.0,>=0.7.0 (from tensorboard~=2.20.0->tensorflow)
  Using cached tensorboard_data_server-0.7.2-py3-none-any.whl.metadata (1.1 kB)
Collecting werkzeug>=1.0.1 (from tensorboard~=2.20.0->tensorflow)
  Using cached werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting contourpy>=1.0.1 (from matplotlib)
  Downloading contourpy-1.3.3-cp313-cp313-macosx_11_0_arm64.whl.metadata (5.5 kB)
Collecting cycler>=0.10 (from matplotlib)
  Using cached cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting fonttools>=4.22.0 (from matplotlib)
  Downloading fonttools-4.60.1-cp313-cp313-macosx_10_13_universal2.whl.metadata (112 kB)
Collecting kiwisolver>=1.3.1 (from matplotlib)
  Downloading kiwisolver-1.4.9-cp313-cp313-macosx_11_0_arm64.whl.metadata (6.3 kB)
Collecting pyparsing>=2.3.1 (from matplotlib)
  Using cached pyparsing-3.2.5-py3-none-any.whl.metadata (5.0 kB)
Requirement already satisfied: python-dateutil>=2.7 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from matplotlib) (2.9.0.post0)
Collecting wheel<1.0,>=0.23.0 (from astunparse>=1.6.0->tensorflow)
  Using cached wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)
Collecting rich (from keras>=3.10.0->tensorflow)
  Using cached rich-14.1.0-py3-none-any.whl.metadata (18 kB)
Collecting namex (from keras>=3.10.0->tensorflow)
  Using cached namex-0.1.0-py3-none-any.whl.metadata (322 bytes)
Collecting optree (from keras>=3.10.0->tensorflow)
  Downloading optree-0.17.0-cp313-cp313-macosx_11_0_arm64.whl.metadata (33 kB)
Collecting MarkupSafe>=2.1.1 (from werkzeug>=1.0.1->tensorboard~=2.20.0->tensorflow)
  Downloading markupsafe-3.0.3-cp313-cp313-macosx_11_0_arm64.whl.metadata (2.7 kB)
Collecting markdown-it-py>=2.2.0 (from rich->keras>=3.10.0->tensorflow)
  Downloading markdown_it_py-4.0.0-py3-none-any.whl.metadata (7.3 kB)
Collecting pygments<3.0.0,>=2.13.0 (from rich->keras>=3.10.0->tensorflow)
  Using cached pygments-2.19.2-py3-none-any.whl.metadata (2.5 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich->keras>=3.10.0->tensorflow)
  Using cached mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Downloading tensorflow-2.20.0-cp313-cp313-macosx_12_0_arm64.whl (200.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200.7/200.7 MB 6.3 MB/s  0:00:31
Downloading grpcio-1.75.1-cp313-cp313-macosx_11_0_universal2.whl (11.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.5/11.5 MB 6.1 MB/s  0:00:01
Downloading ml_dtypes-0.5.3-cp313-cp313-macosx_10_13_universal2.whl (663 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 663.8/663.8 kB 4.9 MB/s  0:00:00
Using cached tensorboard-2.20.0-py3-none-any.whl (5.5 MB)
Using cached tensorboard_data_server-0.7.2-py3-none-any.whl (2.4 kB)
Using cached typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Downloading numpy-2.3.3-cp313-cp313-macosx_14_0_arm64.whl (5.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.1/5.1 MB 6.4 MB/s  0:00:00
Downloading matplotlib-3.10.6-cp313-cp313-macosx_11_0_arm64.whl (8.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.1/8.1 MB 6.7 MB/s  0:00:01
Downloading pillow-11.3.0-cp313-cp313-macosx_11_0_arm64.whl (4.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.7/4.7 MB 5.0 MB/s  0:00:00
Using cached absl_py-2.3.1-py3-none-any.whl (135 kB)
Using cached astunparse-1.6.3-py2.py3-none-any.whl (12 kB)
Using cached wheel-0.45.1-py3-none-any.whl (72 kB)
Downloading contourpy-1.3.3-cp313-cp313-macosx_11_0_arm64.whl (274 kB)
Using cached cycler-0.12.1-py3-none-any.whl (8.3 kB)
Using cached flatbuffers-25.9.23-py2.py3-none-any.whl (30 kB)
Downloading fonttools-4.60.1-cp313-cp313-macosx_10_13_universal2.whl (2.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.8/2.8 MB 5.5 MB/s  0:00:00
Using cached gast-0.6.0-py3-none-any.whl (21 kB)
Using cached google_pasta-0.2.0-py3-none-any.whl (57 kB)
Downloading h5py-3.14.0-cp313-cp313-macosx_11_0_arm64.whl (2.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.8/2.8 MB 6.7 MB/s  0:00:00
Downloading keras-3.11.3-py3-none-any.whl (1.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 5.2 MB/s  0:00:00
Downloading kiwisolver-1.4.9-cp313-cp313-macosx_11_0_arm64.whl (64 kB)
Using cached libclang-18.1.1-1-py2.py3-none-macosx_11_0_arm64.whl (25.8 MB)
Using cached markdown-3.9-py3-none-any.whl (107 kB)
Using cached opt_einsum-3.4.0-py3-none-any.whl (71 kB)
Using cached packaging-25.0-py3-none-any.whl (66 kB)
Using cached pyparsing-3.2.5-py3-none-any.whl (113 kB)
Using cached termcolor-3.1.0-py3-none-any.whl (7.7 kB)
Using cached werkzeug-3.1.3-py3-none-any.whl (224 kB)
Downloading markupsafe-3.0.3-cp313-cp313-macosx_11_0_arm64.whl (12 kB)
Downloading wrapt-1.17.3-cp313-cp313-macosx_11_0_arm64.whl (39 kB)
Using cached namex-0.1.0-py3-none-any.whl (5.9 kB)
Downloading optree-0.17.0-cp313-cp313-macosx_11_0_arm64.whl (354 kB)
Using cached rich-14.1.0-py3-none-any.whl (243 kB)
Using cached pygments-2.19.2-py3-none-any.whl (1.2 MB)
Downloading markdown_it_py-4.0.0-py3-none-any.whl (87 kB)
Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Installing collected packages: namex, libclang, flatbuffers, wrapt, wheel, typing_extensions, termcolor, tensorboard-data-server, pyparsing, pygments, pillow, packaging, opt_einsum, numpy, mdurl, MarkupSafe, markdown, kiwisolver, google_pasta, gast, fonttools, cycler, absl-py, werkzeug, optree, ml_dtypes, markdown-it-py, h5py, grpcio, contourpy, astunparse, tensorboard, rich, matplotlib, keras, tensorflow
Successfully installed MarkupSafe-3.0.3 absl-py-2.3.1 astunparse-1.6.3 contourpy-1.3.3 cycler-0.12.1 flatbuffers-25.9.23 fonttools-4.60.1 gast-0.6.0 google_pasta-0.2.0 grpcio-1.75.1 h5py-3.14.0 keras-3.11.3 kiwisolver-1.4.9 libclang-18.1.1 markdown-3.9 markdown-it-py-4.0.0 matplotlib-3.10.6 mdurl-0.1.2 ml_dtypes-0.5.3 namex-0.1.0 numpy-2.3.3 opt_einsum-3.4.0 optree-0.17.0 packaging-25.0 pillow-11.3.0 pygments-2.19.2 pyparsing-3.2.5 rich-14.1.0 tensorboard-2.20.0 tensorboard-data-server-0.7.2 tensorflow-2.20.0 termcolor-3.1.0 typing_extensions-4.15.0 werkzeug-3.1.3 wheel-0.45.1 wrapt-1.17.3
(venv) medvr05@medvr05s-MacBook-Pro xray-project % which pip3
/Library/Frameworks/Python.framework/Versions/3.13/bin/pip3
(venv) medvr05@medvr05s-MacBook-Pro xray-project % python train_model.py
zsh: command not found: python
(venv) medvr05@medvr05s-MacBook-Pro xray-project % python3 train_model.py
Matplotlib is building the font cache; this may take a moment.
Found 5216 images belonging to 2 classes.
Found 16 images belonging to 2 classes.
Found 624 images belonging to 2 classes.
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Model: "sequential"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ conv2d (Conv2D)                 │ (None, 148, 148, 32)   │           896 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch_normalization             │ (None, 148, 148, 32)   │           128 │
│ (BatchNormalization)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ max_pooling2d (MaxPooling2D)    │ (None, 74, 74, 32)     │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d_1 (Conv2D)               │ (None, 72, 72, 64)     │        18,496 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch_normalization_1           │ (None, 72, 72, 64)     │           256 │
│ (BatchNormalization)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ max_pooling2d_1 (MaxPooling2D)  │ (None, 36, 36, 64)     │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d_2 (Conv2D)               │ (None, 34, 34, 128)    │        73,856 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch_normalization_2           │ (None, 34, 34, 128)    │           512 │
│ (BatchNormalization)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ max_pooling2d_2 (MaxPooling2D)  │ (None, 17, 17, 128)    │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d_3 (Conv2D)               │ (None, 15, 15, 128)    │       147,584 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch_normalization_3           │ (None, 15, 15, 128)    │           512 │
│ (BatchNormalization)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ max_pooling2d_3 (MaxPooling2D)  │ (None, 7, 7, 128)      │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ flatten (Flatten)               │ (None, 6272)           │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout (Dropout)               │ (None, 6272)           │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense (Dense)                   │ (None, 512)            │     3,211,776 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout_1 (Dropout)             │ (None, 512)            │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_1 (Dense)                 │ (None, 1)              │           513 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 3,454,529 (13.18 MB)
 Trainable params: 3,453,825 (13.18 MB)
 Non-trainable params: 704 (2.75 KB)

🚀 Starting training...
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/keras/src/trainers/data_adapters/py_dataset_adapter.py:121: UserWarning: Your `PyDataset` class should call `super().__init__(**kwargs)` in its constructor. `**kwargs` can include `workers`, `use_multiprocessing`, `max_queue_size`. Do not pass these arguments to `fit()`, as they will be ignored.
  self._warn_if_super_not_called()
Traceback (most recent call last):
  File "/Users/medvr05/Desktop/xray-project/train_model.py", line 133, in <module>
    history = model.fit(
        train_generator,
    ...<2 lines>...
        callbacks=callbacks
    )
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/keras/src/utils/traceback_utils.py", line 122, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/keras/src/utils/module_utils.py", line 29, in initialize
    raise ImportError(self.import_error_msg)
ImportError: This requires the scipy module. You can install it via `pip install scipy`
(venv) medvr05@medvr05s-MacBook-Pro xray-project % pip install scipy
zsh: command not found: pip
(venv) medvr05@medvr05s-MacBook-Pro xray-project % pip3 install scipy
Collecting scipy
  Downloading scipy-1.16.2-cp313-cp313-macosx_14_0_arm64.whl.metadata (62 kB)
Requirement already satisfied: numpy<2.6,>=1.25.2 in /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages (from scipy) (2.3.3)
Downloading scipy-1.16.2-cp313-cp313-macosx_14_0_arm64.whl (20.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 20.9/20.9 MB 6.7 MB/s  0:00:03
Installing collected packages: scipy
Successfully installed scipy-1.16.2
(venv) medvr05@medvr05s-MacBook-Pro xray-project % python3 train_model.py
Found 5216 images belonging to 2 classes.
Found 16 images belonging to 2 classes.
Found 624 images belonging to 2 classes.
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/keras/src/layers/convolutional/base_conv.py:113: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)
Model: "sequential"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ conv2d (Conv2D)                 │ (None, 148, 148, 32)   │           896 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch_normalization             │ (None, 148, 148, 32)   │           128 │
│ (BatchNormalization)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ max_pooling2d (MaxPooling2D)    │ (None, 74, 74, 32)     │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d_1 (Conv2D)               │ (None, 72, 72, 64)     │        18,496 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch_normalization_1           │ (None, 72, 72, 64)     │           256 │
│ (BatchNormalization)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ max_pooling2d_1 (MaxPooling2D)  │ (None, 36, 36, 64)     │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d_2 (Conv2D)               │ (None, 34, 34, 128)    │        73,856 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch_normalization_2           │ (None, 34, 34, 128)    │           512 │
│ (BatchNormalization)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ max_pooling2d_2 (MaxPooling2D)  │ (None, 17, 17, 128)    │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ conv2d_3 (Conv2D)               │ (None, 15, 15, 128)    │       147,584 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ batch_normalization_3           │ (None, 15, 15, 128)    │           512 │
│ (BatchNormalization)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ max_pooling2d_3 (MaxPooling2D)  │ (None, 7, 7, 128)      │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ flatten (Flatten)               │ (None, 6272)           │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout (Dropout)               │ (None, 6272)           │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense (Dense)                   │ (None, 512)            │     3,211,776 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout_1 (Dropout)             │ (None, 512)            │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense_1 (Dense)                 │ (None, 1)              │           513 │
└─────────────────────────────────┴────────────────────────┴───────────────┘
 Total params: 3,454,529 (13.18 MB)
 Trainable params: 3,453,825 (13.18 MB)
 Non-trainable params: 704 (2.75 KB)

🚀 Starting training...
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/keras/src/trainers/data_adapters/py_dataset_adapter.py:121: UserWarning: Your `PyDataset` class should call `super().__init__(**kwargs)` in its constructor. `**kwargs` can include `workers`, `use_multiprocessing`, `max_queue_size`. Do not pass these arguments to `fit()`, as they will be ignored.
  self._warn_if_super_not_called()
Epoch 1/10
163/163 ━━━━━━━━━━━━━━━━━━━━ 0s 207ms/step - accuracy: 0.8564 - auc: 0.8870 - loss: 0.7475/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/keras/src/trainers/data_adapters/py_dataset_adapter.py:121: UserWarning: Your `PyDataset` class should call `super().__init__(**kwargs)` in its constructor. `**kwargs` can include `workers`, `use_multiprocessing`, `max_queue_size`. Do not pass these arguments to `fit()`, as they will be ignored.
  self._warn_if_super_not_called()
163/163 ━━━━━━━━━━━━━━━━━━━━ 35s 209ms/step - accuracy: 0.8888 - auc: 0.9245 - loss: 0.4718 - val_accuracy: 0.5000 - val_auc: 0.5000 - val_loss: 26.0359 - learning_rate: 0.0010
Epoch 2/10
163/163 ━━━━━━━━━━━━━━━━━━━━ 34s 210ms/step - accuracy: 0.9204 - auc: 0.9671 - loss: 0.2042 - val_accuracy: 0.5000 - val_auc: 0.5000 - val_loss: 56.4904 - learning_rate: 0.0010
Epoch 3/10
163/163 ━━━━━━━━━━━━━━━━━━━━ 34s 210ms/step - accuracy: 0.9275 - auc: 0.9700 - loss: 0.1951 - val_accuracy: 0.5000 - val_auc: 0.5000 - val_loss: 39.3977 - learning_rate: 0.0010
Epoch 4/10
163/163 ━━━━━━━━━━━━━━━━━━━━ 35s 215ms/step - accuracy: 0.9467 - auc: 0.9824 - loss: 0.1469 - val_accuracy: 0.5000 - val_auc: 0.9375 - val_loss: 1.8582 - learning_rate: 5.0000e-04
Epoch 5/10
163/163 ━━━━━━━━━━━━━━━━━━━━ 37s 228ms/step - accuracy: 0.9526 - auc: 0.9847 - loss: 0.1305 - val_accuracy: 0.5625 - val_auc: 0.6250 - val_loss: 1.4252 - learning_rate: 5.0000e-04
Epoch 6/10
163/163 ━━━━━━━━━━━━━━━━━━━━ 37s 226ms/step - accuracy: 0.9534 - auc: 0.9868 - loss: 0.1245 - val_accuracy: 0.5625 - val_auc: 0.6484 - val_loss: 3.6966 - learning_rate: 5.0000e-04
Epoch 7/10
163/163 ━━━━━━━━━━━━━━━━━━━━ 37s 227ms/step - accuracy: 0.9565 - auc: 0.9868 - loss: 0.1232 - val_accuracy: 0.5625 - val_auc: 0.6875 - val_loss: 10.2243 - learning_rate: 5.0000e-04
Epoch 8/10
163/163 ━━━━━━━━━━━━━━━━━━━━ 37s 224ms/step - accuracy: 0.9588 - auc: 0.9890 - loss: 0.1106 - val_accuracy: 0.7500 - val_auc: 0.7812 - val_loss: 0.7556 - learning_rate: 2.5000e-04
Epoch 9/10
163/163 ━━━━━━━━━━━━━━━━━━━━ 37s 225ms/step - accuracy: 0.9607 - auc: 0.9911 - loss: 0.0996 - val_accuracy: 0.7500 - val_auc: 0.9375 - val_loss: 0.6219 - learning_rate: 2.5000e-04
Epoch 10/10
163/163 ━━━━━━━━━━━━━━━━━━━━ 37s 223ms/step - accuracy: 0.9643 - auc: 0.9911 - loss: 0.0984 - val_accuracy: 0.5625 - val_auc: 0.6875 - val_loss: 4.0243 - learning_rate: 2.5000e-04

📊 Evaluating on test set...
20/20 ━━━━━━━━━━━━━━━━━━━━ 2s 98ms/step - accuracy: 0.8750 - auc: 0.9544 - loss: 0.4015     

Test Accuracy: 0.8750
Test AUC: 0.9544

✅ Model saved successfully!
20/20 ━━━━━━━━━━━━━━━━━━━━ 2s 93ms/step 

🎉 Training and evaluation complete!
(venv) medvr05@medvr05s-MacBook-Pro xray-project % nano README.md

  UW PICO 5.09                    File: README.md                     Modified  

What Could Be Better
Some ideas I'm thinking about:

Try transfer learning with ResNet or EfficientNet
Add Grad-CAM visualizations to see what the model is looking at
Handle the class imbalance better
Cross-validation for more reliable metrics  

Resources

Dataset: Kaggle
Built with TensorFlow and Keras








^G Get Help  ^O WriteOut  ^R Read File ^Y Prev Pg   ^K Cut Text  ^C Cur Pos   
^X Exit      ^J Justify   ^W Where is  ^V Next Pg   ^U UnCut Text^T To Spell  
