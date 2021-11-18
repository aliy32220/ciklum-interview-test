import { shallowMount } from '@vue/test-utils'
import InputField from '@/components/Rating'

describe('InputField', () => {
  // your tests go here
  const wrapper = shallowMount(InputField, {
    propsData: {
      newItemTitle: ""
    } 
  })
  it('gets the input and Store it in prop.newItemTitle', () => {
        expect(wrapper.findAll.length > 0)
  })
})