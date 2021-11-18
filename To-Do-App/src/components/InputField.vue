<template>
  <v-form>
    <v-text-field v-model="newItemTitle"
                  label="What do you need to do?"
                  >
    </v-text-field>
  </v-form>
</template>

<script>
const MIN_LENGTH_VALIDATION = 3

export default {
  name: 'InputField',
  data () {
    return {
      newItemTitle: '',
      rules: {
        minLength: value => {
          return (value.length >= MIN_LENGTH_VALIDATION) || `Required having at least ${MIN_LENGTH_VALIDATION} characters.`
        }
      }
    }
  },
  methods: {
    addTodo () {
      if (this.newItemTitle.length >= MIN_LENGTH_VALIDATION) {
        this.$store.dispatch('addTodo', this.newItemTitle)
        this.newItemTitle = ''
      }
    },
    getlistTitle(){
      return this.newItemTitle;
    },
    clearField()
    {
      this.newItemTitle = "";
    }
  }
}
</script>
