<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-100">
        <div class="bg-white shadow-md rounded p-8 max-w-md w-full mx-auto">
            <h2 class="text-2xl font-bold mb-4 text-gray-800">Sign Up</h2>
            <form @submit.prevent="signUp">
                <div class="mb-4">
                    <input type="text" v-model="username"
                           placeholder="Username"
                           class="w-full border border-gray-300 rounded py-2 px-4 leading-tight focus:outline-none focus:border-gray-500" />
                </div>
                <div class="mb-4">
                    <input type="email" v-model="email"
                           placeholder="Email"
                           class="w-full border border-gray-300 rounded py-2 px-4 leading-tight focus:outline-none focus:border-gray-500" />
                </div>
                <div class="mb-4">
                    <input type="password" v-model="password"
                           placeholder="Password"
                           class="w-full border border-gray-300 rounded py-2 px-4 leading-tight focus:outline-none focus:border-gray-500" />
                </div>
                <div class="mb-6">
                    <input type="password"
                           v-model="confirmPassword"
                           placeholder="Confirm Password"
                           class="w-full border border-gray-300 rounded py-2 px-4 leading-tight focus:outline-none focus:border-gray-500" />
                </div>
                <button type="submit"
                        class="w-full bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 rounded-md focus:outline-none">Sign Up</button>
            </form>
            <p class="mt-4 text-sm text-center text-gray-600">Already have an account? <a href="/login"
                                                                                         class="text-blue-500 hover:underline">Sign in here</a></p>
        </div>
    </div>
</template>

<script>
    import apiClient from '../services/api';

    export default {
        data() {
            return {
                username: '',
                email: '',
                password: '',
                confirmPassword: ''
            }
        },
        methods: {
            async signUp() {
                if (this.username.trim() === "" || this.email.trim() === "" ||
                    this.password.trim() === "" || this.confirmPassword.trim() === "") {
                    alert("Please fill in all fields.");
                    return;
                }
                if (this.password !== this.confirmPassword) {
                    alert("Passwords do not match.");
                    return;
                }
                try {
                    await apiClient.post('signup/', {
                        username: this.username,
                        email: this.email,
                        password: this.password
                    });
                    alert("Sign up successful!");
                    this.username = '';
                    this.email = '';
                    this.password = '';
                    this.confirmPassword = '';
                } catch (error) {
                    console.error('Sign up failed:', error);
                    alert("Sign up failed. Please try again.");
                }
            }
        }
    };
</script>
