# PR Annotator Examples

## Example 1: Basic Annotation

### Input

**Repo:** `acme/payments-api`
**PR:** `#42`
**Base branch:** `main`

**Description:**
```markdown
### Changes

- Added `MAX_RETRIES` (3) and `BASE_DELAY_MS` (2000) constants
- Imported `PaymentService` and injected it into constructor
- Replaced inline fetch calls with `this.paymentService.process()`
```

### Agent Workflow

**Step 1 — Changed files:**
```
apps/api/src/billing/billing.service.ts
```

**Step 2 — Hash computation:**
```
apps/api/src/billing/billing.service.ts -> a1b2c3d4...
```

**Step 3 — Line mapping:**
```
MAX_RETRIES, BASE_DELAY_MS    -> R22-R23
PaymentService import          -> R5
PaymentService constructor     -> R31
Replaced fetch with service    -> R85-R92
```

### Output

```markdown
### Changes

- Added `MAX_RETRIES` (3) and `BASE_DELAY_MS` (2000) constants [[1]](https://github.com/acme/payments-api/pull/42/files#diff-a1b2c3d4R22-R23)
- Imported `PaymentService` and injected it into constructor [[1]](https://github.com/acme/payments-api/pull/42/files#diff-a1b2c3d4R5) [[2]](https://github.com/acme/payments-api/pull/42/files#diff-a1b2c3d4R31)
- Replaced inline fetch calls with `this.paymentService.process()` [[1]](https://github.com/acme/payments-api/pull/42/files#diff-a1b2c3d4R85-R92)
```

---

## Example 2: Mixed Additions and Removals

### Input

**Description:**
```markdown
### `apps/mobile/lib/auth.ts`

- Added `registerIdentity(userId)` helper function
- Removed duplicate identity calls from `handleLogin()`

### `apps/mobile/screens/login.tsx`

- Removed `import { Identity } from 'identity-sdk'`
- Removed all inline `Identity.login()` calls
```

### Output

```markdown
### `apps/mobile/lib/auth.ts`

- Added `registerIdentity(userId)` helper function [[1]](https://github.com/acme/app/pull/99/files#diff-f5e6a7b8R31-R55)
- Removed duplicate identity calls from `handleLogin()`

### `apps/mobile/screens/login.tsx`

- Removed `import { Identity } from 'identity-sdk'` [[diff]](https://github.com/acme/app/pull/99/files#diff-c9d0e1f2)
- Removed all inline `Identity.login()` calls [[diff]](https://github.com/acme/app/pull/99/files#diff-c9d0e1f2)
```

Note: The removal bullet under `auth.ts` ("Removed duplicate identity calls") has no link because it describes deleted code within a modified file where no new lines correspond. The `login.tsx` removals link to the file-level diff since the entire change is deletions.

---

## Example 3: New Test File

### Input

**Description:**
```markdown
### `apps/api/src/billing/billing.service.spec.ts` (new)

- Tests `processPayment`: validates input, retries on timeout, throws on invalid amount
- Uses `jest.useFakeTimers()` for deterministic retry delays
- Mocks `PaymentGateway` to avoid real API calls
```

### Output

```markdown
### `apps/api/src/billing/billing.service.spec.ts` (new)

- Tests `processPayment`: validates input, retries on timeout, throws on invalid amount [[1]](https://github.com/acme/payments-api/pull/42/files#diff-b3c4d5e6R40-R120)
- Uses `jest.useFakeTimers()` for deterministic retry delays [[1]](https://github.com/acme/payments-api/pull/42/files#diff-b3c4d5e6R15)
- Mocks `PaymentGateway` to avoid real API calls [[1]](https://github.com/acme/payments-api/pull/42/files#diff-b3c4d5e6R8-R12)
```

Note: For new files, all lines are right-side (`R`) lines since the entire file is an addition.
