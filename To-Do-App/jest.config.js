module.exports = {
    preset: '@vue/cli-plugin-unit-jest',
    modulePaths: [
      "<rootDir>/src",
      "<rootDir>/node_modules"
    ],
    globals: {
      "NODE_ENV": "test"
    },
    verbose: true,
    moduleFileExtensions: [
      "ts",
      "tsx",
      "js",
      "jsx",
      "json"
    ],
    transformIgnorePatterns: [
      "node_modules/@babel/runtime/helpers/esm/(?!interopRequireDefault.js)",
    ],
    transform: {
      "\\.[jt]sx?$": "D:/ciklum-interview-test/To-Do-App/node_modules/@babel/runtime/helpers/esm/typeof"
    },
    testEnvironment: "node",
    moduleNameMapper: {
      "^typeof$": "typeof"
    }
  };