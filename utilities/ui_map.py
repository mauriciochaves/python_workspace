home_page = dict(
    searchFieldByID="search_query_top",
    searchButtonByName="submit_search",
    cartButtonCSSSelector="a b",
    dressesButtonByXpath="(//a[@class='sf-with-ul'])[4]",
    dressesButtonActivateByXpath="(//ul[@class='submenu-container clearfix first-in-line-xs'])[2]",
    dressesButtonCassualDressesByXpath="(//a[@title='Summer Dresses'])[2]",
    womenButtonByXpath="//a[@title='Women']"
)

product_page = dict(
    selectProductByClassName="replace-2x",
    hoverOverProductBoxByClassName="right-block",
    productAddButtonByXpath="//span[contains(text(), 'Add to cart')]",
    modalWindowByXpath="//i[@class='icon-chevron-left left']"
)

shopping_cart = dict(
    blouseItemInTheCartByLinkText="Blouse",
    pinnedSummerDressByLinkText="Printed Summer Dress",
    pinnedChiffonDress="Printed Chiffon Dress"
)

dresses_page = dict(
    summerDressesImageButtonByXpath="(//a[@title='Summer Dresses'])[3]",
    locateAllProductsByXpath="//div[@class='right-block']",
    addProductsToCartByXpath="//a[@title='Add to cart']",

    scrollIntoViewByXpath="//ul[@class='product_list grid row']",
    hoverAllElementsByXpath="(//div[@class='right-block'])",
    locateSelectedElementsByXpath="(//div[@class='right-block'])[{0}]",
    productAddButtonByXpath="(//span[contains(text(), 'Add to cart')])[{0}]"
)
