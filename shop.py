from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def clothes_shop():
    return render_template('shop.html')

@app.route('/clothes/')
def clothes():
    clothes = {
        'name' : 'название товара',
        'sizes' : 'размеры',
        'slae' : 'в продаже'
    }

    clothes_list = [
        {
            'name' : 'blouse',
            'sizes' : 'S, M, L, XL, XXL ',
            'sale' : 15
        },
        {
            'name' : 'jeans',
            'sizes' : 'S, M, L, XL',
            'sale' : 13
        },
    ]

    return render_template('index_1_clothes.html', **clothes, clothes_list=clothes_list)

@app.route('/shoes/')
def shoes():
    shoes = {
        'name' : 'название товара',
        'sizes' : 'размеры',
        'slae' : 'в продаже'
    }

    shoes_list = [
        {
            'name' : 'Обувь',
            'sizes' : '25-45',
            'sale' : 45
        }
    ]

    return render_template('index_1_shoes.html',**shoes, shoes_list=shoes_list)

@app.route('/jackets/')
def jackets():
    jackets = {
        'name' : 'название товара',
        'sizes' : 'размеры',
        'slae' : 'в продаже'
    }

    jackets_list = [
        {
            'name' : 'Куртки',
            'sizes' : 'S, M, L, XL, XXL ',
            'sale' : 15
        }
    ]

    return render_template('index_1_jackets.html',**jackets, jackets_list=jackets_list)


if __name__ == '__main__':
    app.run(debug=True)