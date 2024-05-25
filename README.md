# pokemon-classification
A pokemon classification!

## Getting Started

Install python & etc.

## Usage

```bash
$ python classify.py <image file name>
```

## Objective

Classify a given image into a pokemon. It's fun!

e.g. Kirby, a person, etc.

## Implementation Strategy

1. Use available datasets here:
   - https://www.kaggle.com/datasets/hlrhegemony/pokemon-image-dataset
   - https://www.kaggle.com/datasets/lantian773030/pokemonclassification
2. Use the CNN model I learned in AIP2 recently.
3. Use the pretrained model VGG-16 in image identification.

## Challenges and Overcoming

- Image preprocessing
  - Challenges: I had a hard time facing challenges on how to resize the image data.
  - Overcoming: I used ChatGPT to overcome this issue. (The '0. Data Preparation' describes this.)
- Training Speed
  - Challenges: I did not notice that the Colab would be more faster than my Jupyter Notebook.
  - Overcoming: Noticed after trying and experiencing.
- Limited Data
  - Challenges: there were 10000 images with 901 pokemons, which seems to be a small amount of data.
  - Overcoming: I tried to use the VGG-16 to overcome this issue!
- Loading drive data into colab notebook
  - Challenges: This takes like 6'53" or so in colab, while it takes much much less in the local desktop.
  - Overcoming: Ask GPT for a parallel loading code, and waited...

## Things to Boast

I never tried CNN or image resizing myself (actually I have a homework related, but not yet finished...LOL), but I did it! (although it had 70% accuracy)
