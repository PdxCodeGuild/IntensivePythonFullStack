Vue.component('add-todo', {
    data: function() {
        return {
            text: "",
            id: 4,
        }
    },
    template: `
        <div>
            <input type="text" placeholder="add a todo" v-model="text" @keyup.enter="addTodo">
            <button @click="addTodo">Add To List</button>
        </div>
    `,
    methods: {
        addTodo: function() {
            this.$emit('add', {id: this.id, text: this.text, completed: false})
            this.id++
            this.text = ""
        }
    }
})

Vue.component('todo-item', {
    data: function() {
        return {
            editMode: false
        }
    },
    props: ['todo'],
    template: `
        <li>
            <input v-if="editMode" type="text" v-model="todo.text" @keyup.enter="editMode = false">
            <template v-else>{{ todo.text }}</template>
            <input type="checkbox" v-model="todo.completed">
            <button @click="editMode = !editMode">{{ editMode ? "Done" : "Edit" }}</button>
            <!-- <button @click="toggleTodo(todo)">✓</button> -->
            <!-- <button @click="removeTodo(todo)">×</button> -->
            <button @click="$emit('remove', todo)">×</button>
        </li>
    `,
    methods: {
        removeTodo: function(todo) {
            this.$emit('remove', todo)
        },
        toggleTodo: function(todo) {
            this.$emit('toggle', todo)
        }
    }
})

const vm = new Vue({
    el: "#app",
    data: {
        todos: [
            {id: 1, text: "Wag the dog", completed: false},
            {id: 2, text: "Butter the cat", completed: true},
            {id: 3, text: "Pick up the milk", completed: false}
        ]
    },
    computed: {
        incompleteTodos: function() {
            // let incompleteTodos = []
            // for (let i=0; i < this.todos.length; i++) {
            //     if (!this.todos[i].completed) {
            //         incompleteTodos.push(this.todos[i])
            //     }
            // }
            // return incompleteTodos
            return this.todos.filter(function(todo) {
                return !todo.completed
            })
        },
        completeTodos: function() {
            // let completeTodos = []
            // for (let i=0; i < this.todos.length; i++) {
            //     if (this.todos[i].completed) {
            //         completeTodos.push(this.todos[i])
            //     }
            // }
            // return completeTodos
            return this.todos.filter(function(todo) {
                return todo.completed
            })
        }
    },
    methods: {
        addTodo: function(todo) {
            this.todos.push(todo)
        },
        removeTodo: function(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)
        },
        toggleTodo: function(todo) {
            // // if (todo.completed) {
            // //     todo.completed = false
            // // } else {
            // //     todo.completed = true
            // // }
            // todo.completed = todo.completed ? false : true
            todo.completed = !todo.completed
        }
    }
})