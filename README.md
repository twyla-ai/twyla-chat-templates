# Twyla Chat Templates
A collection of Twyla chat message templates

## Installation
`poetry install twyla-chat-templates`

## Usage

##### Quick reply buttons
```python
quick_replies = QuickReplies(text="Which kind of chocolate do you prefer?")

# To add up to ten quick reply buttons:
quick_replies.add(QuickReply(title="Dark", payload="dark_chocolate"))
```

##### Postback and URL Buttons
```python
buttons = Buttons(text="What is your favourite type of pizza?")

# To add up to three buttons:
buttons.add(
        PostBackButton(title="Margherita", payload="x_Margherita_oaWVAeasEK_x"),
        UrlButton(title="Hawaii", url="https://google.com"),
    )
```
##### Generic Template
```python
element = GenericElement(
        title="Cheesecake",
        subtitle="Cake with cheese",
        image_url="https://cake.com/image.jpg",
        action_url="https://cake.com",
        buttons=[
            PostBackButton(
                title="I want Cheesecake", payload="x_I_want_Cheesecake_gkvMPBXXxO_x"
            ),
            UrlButton(title="Cheesecake, please", url="https://cheesecakeplease.com"),
        ],
    )
template =  GenericTemplate(elements=[element])
```
##### Carousel Template
```python
# To Create a vertically scrollable carousel, add up to 10 elements to the generic template: 
carousel = GenericTemplate(elements=[e1, e2, e3])
```

##### Image Template 
```python
image = ImageTemplate(url="https://pictures.com/picture.jpg")
```
