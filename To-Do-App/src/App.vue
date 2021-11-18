<template>
  <v-app>
    <v-flex xs12 sm6 offset-sm3>
      <v-card>
        <v-card-title primary-title class="title">
          <div>
            <h3 class="mat-h2 mb-0">Todo List</h3>
          </div>
        </v-card-title>
        <v-card-text>
          <TodoItem v-for="(todo, index) in todos"
                    :key="index"
                    :todo="todo">
          </TodoItem>
          <InputField ref="inputFeild"></InputField>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="success" @click="insertlists">Save Item</v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-app>
</template>

<script>
import TodoItem from './components/TodoItem'
import InputField from './components/InputField'
import config from './config/config.json'
import axios from 'axios'
axios.defaults.headers.get['Access-Control-Allow-Origin'] = '*';
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

export default {
  name: 'App',
  components: {
    TodoItem,
    InputField
  },
  data () {
    return {
      todoslist: [],
      config: { headers: { 'Accept': 'application/json', 'Content-Type':'application/json' }},
      todos (){
        this.todoslist;
      }
    }
  },
  async created()
  {
      this.getlists();
  },
  methods: {
    async getlists(){
      var data = {}
        await axios.post('http://127.0.0.1:8000/get-lists', data, this.config).then( async(response) => {
          console.log(response.data.Data[0]["ToDo"]);
          for(var i = 0; i<response.data.Data.length; i++)
          { 
              this.todoslist.push(response.data.Data[i]['ToDo']);
          }
          console.log(this.todoslist[0]);
      }).catch((error) => {
          console.log("Error in Getting Lists", error);
      });
    },
    async insertlists(){
      console.log(this.todos)
      var title = this.$refs.inputFeild.getlistTitle()
      var data = {
          Title :  title
        }
        await axios.post('http://127.0.0.1:8000/insert-lists', data, this.config).then( async(response) => {
          console.log(response);
          this.todoslist.push(title)
          this.$refs.inputFeild.clearField()
      }).catch((error) => {
          console.log("Error in inserting Lists", error);
      });
    }
  }
}
</script>

<style>
  .title {
    display: flex;
    justify-content: center;
  }
</style>
