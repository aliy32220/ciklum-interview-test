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
    transform: {
      "^.+\\.jsx?$": "babel-jest",
      "^.+\\.tsx?$": "<rootDir>/node_modules/@babel/runtime/helpers/esminteropRequireDefault.js"
    },
    transformIgnorePatterns: [
      "/node_modules/(?!interoprequireDefault)"
    ],
    testRegex: "test/.*\\.spec\\.ts$",
    testEnvironment: "node",
    moduleNameMapper: {
      "^interopRequireDeafault$": "interopRequireDeafault"
    }
  };