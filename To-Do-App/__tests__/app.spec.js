import { mount } from '@vue/test-utils'
import App from './../src/App.vue'

it('has a button', () => {
    expect(wrapper.find('button').exists()).toBe(true)
  })

it('has a text area', () => {
expect(wrapper.find('text area').exists()).toBe(true)
})

describe('App', () => {
    // Inspect the raw component options
    it('has data', () => {
      expect(App.data).toBe('function')
    })
  })
describe('App', () => {
    it('has created', () => {
        expect(App.created).toBe('function')
    })
})
  