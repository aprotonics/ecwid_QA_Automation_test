let searchButtonSelector = '#static-html a.footer__link--all-products'
let filtersSelector = '.ec-filters__wrap .ec-filter--offers .form-control__inline-label'
let productPricesSelector = '.grid__products .grid-product .grid-product__price-value'
let cartButtonSelector = '.details-product-purchase__add-buttons .form-control:last-child button.form-control__button'
let cartSpanSelector = '.details-product-purchase__add-buttons .form-control:last-child button.form-control__button span.form-control__button-text'
let cartIconSelector = '.float-icons__icon--cart > .ec-cart-widget > .ec-minicart'
let emailInputSelector = '#ec-cart-email-input'
let checkboxAgreeSelector = '#form-control__checkbox--agree'
let placeOrderButtonSelector = '.form-control__button > .form-control__loader'
let nameInputSelector = '#ec-full-name'
let addressInputSelector = '#ec-address-line1'
let cityInputSelector = '#ec-city-list'
let postalInputSelector = '#ec-postal-code'
let placeOrderButton2Selector = '.form-control__button > .form-control__loader'
let thanksBlockSelector = 'div.ec-store__confirmation-page h1.page-title__name'

let emailInputValue = 'test@mail.ru'
let nameInputValue = 'test'
let addressInputValue = 'test'
let cityInputValue = 'test'
let postalInputValue = '100000'

let timeInterval = 200


async function loadScript(url) {
  let response = await fetch(url);
  let script = await response.text();
  eval(script);
}

async function fillInput(input, value) {
  input.value = value;
  await input.dispatchEvent(new KeyboardEvent('keydown', { bubbles: true }));
  await input.dispatchEvent(new KeyboardEvent('keypress', { bubbles: true }));
  await input.dispatchEvent(new KeyboardEvent('keyup', { bubbles: true }));
  await input.dispatchEvent(new Event('input', { bubbles: true }));
  await input.dispatchEvent(new Event('change', { bubbles: true }));
}

function mainPage() {
  let searchButton
  let timeSearchButton


  timeSearchButton = setInterval(findSearchButton, timeInterval)

  function findSearchButton() {
    searchButton = document.querySelector(searchButtonSelector)
    if (searchButton) {
      clearInterval(timeSearchButton)
      clickSearchButton()
    }
  }

  function clickSearchButton() {
    searchButton.click()
  }

}

function searchPage() {
  let filters
  let productPrices
  let productPrice
  let timerFilters
  let timerProductPrices


  timerFilters = setInterval(findFilters, timeInterval)

  function findFilters() {
    filters = document.querySelector(filtersSelector)
    if (filters) {
      clearInterval(timerFilters)
      timerProductPrices = setInterval(findProductPrice, timeInterval)
    }
  }

  function findProductPrice() {  
    productPrices = document.querySelectorAll(productPricesSelector)
    if (productPrices) {
      clearInterval(timerProductPrices)

      for (i = 0; i < productPrices.length; i++) {
        price = parseFloat(productPrices[i].textContent.split("$")[1])
        if (price == 0.00) {
          productPrice = productPrices[i]
          break
        } 
      }
      clickProduct()
    }
  }

  function clickProduct() {
    productPrice.click()
  }

}

function productPage() {
  let cartSpan
  let cartButton
  let cartIcon
  let timerCartSpan
  let timerCartButton
  let timerCartIcon


  timerCartSpan = setInterval(findCartSpan, timeInterval)

  function findCartSpan() {
    cartSpan = document.querySelector(cartSpanSelector)
    if (cartSpan) {
      clearInterval(timerCartSpan)
      timerCartButton = setInterval(findCartButton, timeInterval)
    }
  }

  function findCartButton() {
    cartButton = document.querySelector(cartButtonSelector)
    if (cartButton) {
      clearInterval(timerCartButton)
      clickCartButton()
      timerCartIcon = setInterval(findCartIcon, timeInterval)
    }
  }

  function clickCartButton() {
    cartButton.click()
  }

  function findCartIcon() {
    cartIcon = document.querySelector(cartIconSelector)
    if (cartIcon) {
      clearInterval(timerCartIcon)
      clickCartIcon()
    }
  }

  function clickCartIcon() {
    cartIcon.click()
  }
  
}

function cartPage() {
  let emailInput
  let checkboxAgree
  let placeOrderButton
  let timerCheckboxAgree
  let timerPlaceOrderButon

  let timerEmailInput = setInterval(findEmailInput, timeInterval)

  function findEmailInput() {
    emailInput = document.querySelector(emailInputSelector)
    if (emailInput) {
      clearInterval(timerEmailInput)
      fillInput(emailInput, emailInputValue)
      timerCheckboxAgree = setInterval(findCheckboxAgree, timeInterval)
    }
  }

  function findCheckboxAgree() {
    checkboxAgree = document.querySelector(checkboxAgreeSelector)
    if (checkboxAgree) {
      clearInterval(timerCheckboxAgree)
      checkboxAgree.click()
      timerPlaceOrderButon = setInterval(findPlaceOrderButton, timeInterval)
    }
  }

  function findPlaceOrderButton() {
    placeOrderButton = document.querySelector(placeOrderButtonSelector)
    if (placeOrderButton) {
      clearInterval(timerPlaceOrderButon)
      placeOrderButton.click()
    }
  }
}

function checkoutPage() {
  let nameInput
  let addressInput
  let cityInput
  let postalInput
  let placeOrderButton2
  let timerNameInput
  let timerAddressInput
  let timerCityInput
  let timerPostalInput
  let timerPlaceOrderButon2

  timerNameInput = setInterval(findNameInput, timeInterval)

  function findNameInput() {
    nameInput = document.querySelector(nameInputSelector)
    if (nameInput) {
      clearInterval(timerNameInput)
      fillInput(nameInput, nameInputValue)
      timerAddressInput = setInterval(findAddressInput, timeInterval)
    }
  }

  function findAddressInput() {
    addressInput = document.querySelector(addressInputSelector)
    if (addressInput) {
      clearInterval(timerAddressInput)
      fillInput(addressInput, addressInputValue)
      timerCityInput = setInterval(findCityInput, timeInterval)
    }
  }

  function findCityInput() {
    cityInput = document.querySelector(cityInputSelector)
    if (cityInput) {
      clearInterval(timerCityInput)
      fillInput(cityInput, cityInputValue)
      timerPostalInput = setInterval(findPostalInput, timeInterval)
    }
  }

  function findPostalInput() {
    postalInput = document.querySelector(postalInputSelector)
    if (postalInput) {
      clearInterval(timerPostalInput)
      fillInput(postalInput, postalInputValue)
      timerPlaceOrderButon2 = setInterval(findPlaceOrderButton, timeInterval)
    }
  }

  function findPlaceOrderButton() {
    placeOrderButton2 = document.querySelector(placeOrderButton2Selector)
    if (placeOrderButton2) {
      clearInterval(timerPlaceOrderButon2)
      placeOrderButton2.click()
    }
  }
}

function assertPage(time) {
  let thanksBlock
  let thanksText
  let timerThanksBlock


  timerThanksBlock = setInterval(findThanksBlock, timeInterval, time)

  function findThanksBlock(time) {
    thanksBlock = document.querySelector(thanksBlockSelector)
    if (thanksBlock) {
      clearInterval(timerThanksBlock)
      makeAssertion(time)
    }
  }
  
  function makeAssertion(time) {
    thanksText = thanksBlock.textContent
    
    let resultMessage = 'Test passed!'
    try {
      chai.assert.include(thanksText, 'Спасибо за заказ')
    }
    catch(error) {
      resultMessage = 'Test failed!'
    }
    finally {
      console.log(resultMessage)
    }

    time = performance.now() - time;
    console.log('Время выполнения = ', time, ' мс');
  }

}

async function run() {
  let time = performance.now()
  
  let scriptUrl = 'https://cdnjs.cloudflare.com/ajax/libs/chai/3.5.0/chai.js'
  loadScript(scriptUrl)

  await mainPage()

  await searchPage()

  await productPage()

  await cartPage()

  await checkoutPage()

  await assertPage(time)
}

run()
