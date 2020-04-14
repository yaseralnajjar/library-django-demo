// https://medium.com/simply-web-development/how-to-create-fluent-interfaces-the-easy-way-with-vanilla-javascript-2a61b6558f01

// htmlElement constructor
export function htmlElement(element) {
  this.element = (element instanceof HTMLElement) ? element : document.createElement(element)
}

// Static method that calls constructor
// and returns chainable object
htmlElement.create = function (elem) {
  return new htmlElement(elem)
}

// Add id
htmlElement.prototype.addId = function (id) {
  if (id) this.element.id = id
  return this
}

// Add a single class
htmlElement.prototype.addClass = function (className) {
  className && this.element.classList.add(className)
  return this
}

// Add multiple classes. Use of rest parameter
// allows classNames to be either a comma-
// separated list or an array of args.
htmlElement.prototype.addClasses = function (...classNames) {
  for (const className of classNames) {
    this.addClass(className)
  }

  return this
}

// Add text content to element
htmlElement.prototype.addTextContent = function (text = '') {
  this.element.textContent = text
  return this
}

// Add single child element and append to parent
htmlElement.prototype.addChild = function (args = {}) {
  const child = htmlElement.create(args.elem)
    .addId(args.id)
    .addClasses(args.classes) // addClasses can take an array or a comma-separated list
    .addTextContent(args.text)
    .addChildren(args.children)

  this.append(child)
  return this
}

// Add multiple child elements
// Takes array of objects
htmlElement.prototype.addChildren = function (children = []) {
  for (const child of children) {
    this.addChild(child)
  }

  return this
}

// Gets child of the current htmlElement and
// wraps it in an instance of htmlElement
htmlElement.prototype.getChild = function (selector) {
  return new htmlElement(this.element.querySelector(selector))
}

// Appends an htmlElement's inner element property
// to the current htmlElement. Not chainable,
// but would be if you add return this.
htmlElement.prototype.append = function (htmlElement) {
  this.element.appendChild(htmlElement.element)
}

// Appends the current htmlElement's inner
// element property to a DOM element.
// Return this to make chainable.
htmlElement.prototype.appendTo = function (domElement) {
  domElement.appendChild(this.element)
}